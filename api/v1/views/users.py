#!/usr/bin/env python3
""" User API endpoints """
from models.user import User
from models.engine.db import DB
from api.v1.views import app_views
from api.v1.auth import auth
from api.v1.auth.utils import (
    token_required, authenticate,
    hash_password, generate_uuid
)
from flask import jsonify, request, abort, make_response
from api.v1.auth import Auth

db = DB()
AUTH = Auth()


@app_views('/users', methods=['GET'], strict_slashes=False)
def all_users():
    """ Retrieves all user objects """
    users = db.all(User)
    return jsonify([user.to_dict() for user in users]), 200

@app_views('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a specific user """
    user = db.find_user_by(id=user_id)

    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ Updates a user object that matches the merchant_id """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    try:
        user = db.update_user(**data)
    except ValueError:
        abort(404)

    return make_response(jsonify(user.to_dict()), 200)

@app_views('/users/<user_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user object that matches the user_id """
    user = db.find_user_by(id=user_id)

    if not user:
        abort(404)

    db.delete(user)
    db.save()

    return make_response(jsonify({}), 200)

@auth('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Geerates reset password token """
    data = request.get_json()
    
    if not data:
        abort(400, description="Not a valid JSON")

    email = data.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email
            "reset_token": reset_token,
        }), 200
    except Exception:
        abort(403)

@auth('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update user password """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    email = data.get("email")
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)
