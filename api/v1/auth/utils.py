#!/usr/bin/env python3
""" Helper functions """
from flask import Flask, request, jsonify, make_response
from api.v1.auth import auth_instance
from functools import wraps



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
