#!/usr/bin/env python3
""" AUTH class """
from models import storage
from flask import jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
import uuid


def generate_uuid():
    """ Generates a string of uuid and returns a string """
    return str(uuid.uuid4())

class AUTH:
    """ AUTH class handles the authentication of users """

    def __init__(self, token_expiry_hours=2):
        """Initialize the AUTH class with token expiry time in hours."""
        self.token_expiry_hours = token_expiry_hours

    def hash_password(self, password):
        """ Hashes the password string """
        return generate_password_hash(password)

    def check_password(self, hashed_password, password):
        """ Checks if the password is the same with the hashed password """
        return check_password_hash(hashed_password, password)

    def register_user(self, **data):
        """Register a new user and assign a role."""

        data['password'] = self.hash_password(data.get('password'))
        user = User(**data)
        user.save()

        return jsonify({"msg": "User registered successfully"}), 201

    def login_user(self, username, password):
        """Authenticate user, return JWT token with role."""
        user = storage.get_by(username=username, password=password)

        if not user or not self.check_password(user["password"], password):
            return make_response(jsonify({"msg": "Invalid username or password"}), 401)

        # Create JWT token with the user role
        access_token = create_access_token(identity=user.id,
                                           additional_claims={"role": user.role},
                                           expires_delta=timedelta(hours=self.token_expiry_hours))

        # Set JWT token in cookie
        response = {"msg": "Login successful"}
        response_object = make_response(jsonify(response), 200)
        set_access_cookies(response_object, access_token)
        return response_object

    def get_reset_password_token(self, email):
        """ returns a token to reset password """
        user = storage.get_by(email=email)
        if not user:
            abort(404)

        token = generate_uuid()
        setattr(user, 'reset_token', token)

        return user.reset_token

    def update_password(self, reset_token, password):
        """ update user password """
        user = storage.get_by(reset_token=reset_token)
        if not user:
            abort(404)

        hashed_password = self.hash_password(password)
        setattr(user, 'password', hashed_password)

        return None
