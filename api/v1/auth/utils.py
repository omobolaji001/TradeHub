#!/usr/bin/env python3
""" Helper functions """
from flask import Flask, request, jsonify, make_response
from auth import Auth
from functools import wraps

auth = Auth()


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
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)
    return decorated
