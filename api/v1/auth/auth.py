#!/usr/bin/env python3
import bcrypt
import uuid
import jwt
import datetime
import os
from dotenv import load_dotenv
from typing import Union
from models.user import User
from models.engine.db import DB
from sqlalchemy.orm.exc import NoResultFound

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
# Simple in-memory blacklist. In production, use a database or cache.
JWT_BLACKLIST = set()


def _hash_password(password: str) -> bytes:
    """Hashes a password string and returns it in bytes form."""
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a string of new uuid and returns the string."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication system."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if they don't already exist."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user credentials."""
        try:
            user = self._db.find_user_by(email=email)
            encoded_password = password.encode('utf-8')
            return bcrypt.checkpw(encoded_password, user.hashed_password)
        except Exception:
            return False

    def generate_jwt(self, email: str) -> str:
        """Generates a JWT token for the user."""
        try:
            user = self._db.find_user_by(email=email)
            payload = {
                "user_id": user.id,
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return token
        except Exception:
            return None

    def verify_jwt(self, token: str) -> Union[dict, None]:
        """ Verifies the JWT token and returns the payload if valid,
        or None if invalid.
        """
        try:
            # Check if the token is in the blacklist
            if token in JWT_BLACKLIST:
                return None

            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def get_user_from_jwt(self, token: str) -> Union[User, None]:
        """Retrieves the user based on the JWT token."""
        payload = self.verify_jwt(token)
        if payload:
            try:
                user = self._db.find_user_by(id=payload["user_id"])
                return user
            except NoResultFound:
                return None
        return None

    def logout(self, token: str) -> None:
        """Logs the user out by adding the token to the blacklist."""
        JWT_BLACKLIST.add(token)  # Add token to the blacklist

    def get_reset_password_token(self, email: str) -> str:
        """Returns a token to reset the password."""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return user.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates the user's password."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError
