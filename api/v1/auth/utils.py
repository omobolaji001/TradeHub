#!/usr/bin/env python3
""" Helper functions """
from flask import Flask, request, jsonify, make_response
from auth import Auth
from functools import wraps
import bcrypt
import uuid

auth = Auth()


def hash_password(password):
    """Hashes a password string and returns it in bytes form
    """
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


def generate_uuid():
    """Generates a string of new uuid and returns the string
    """
    return str(uuid.uuid4())


def token_required(f):
    """Decorator to check if the JWT token is valid."""
    @wraps(f)
    def decorated(*args, **kwargs):
        # Get token from header
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # 'Bearer token'
            token = token.split(" ")[1]
            data = auth.verify_jwt(token)

            if data is None:
                return jsonify({'message': 'Token is invalid!'}), 401

            g.user_id = data["user_id"]

        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)
    return decorated


def authorize(required_role: str):
    """Decorator to check if the user has the required role."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                token = token.split(" ")[1]  # 'Bearer token'
                payload = auth.verify_jwt(token)
                if payload is None:
                    return jsonify({'message': 'Token is invalid!'}), 401

                user_role = payload.get('role')
                if user_role != required_role:
                    return jsonify({'message': 'You are not authorized to access this route!'}), 403
            except Exception as e:
                return jsonify({'message': 'Token is invalid!'}), 401

            return f(*args, **kwargs)
        return decorated_function
    return decorator
