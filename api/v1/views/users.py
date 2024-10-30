#!/usr/bin/env python3
""" User API endpoints """
from models.user import User
from models import storage
from api.v1.views import app_views, auth
from api.v1.auth.utils import authorize
from flask import jsonify, request, abort, make_response
from api.v1.auth import auth_instance
from flask_jwt_extended import jwt_required


@auth.route('/register', methods=['POST'], strict_slashes=False)
def register_users():
    """ Register new user """
    data = request.get_json()
    if not data:
        abort(400, description="Not a valid JSON")

    valid_roles = ["admin", "merchant", "customer"]

    role = data.get("role", None)
    if role and role not in valid_roles:
        return jsonify({"error": f"Invalid user role {role}"}), 400

    response = auth_instance.register_user(**data)

    return response

@auth.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """ user login """
    data = request.get_json()
    if not data:
        abort(400, description="Not a valid JSON")

    username = data.get('username')
    password = data.get('password')

    response = auth_instance.login_user(username, password)

    return response

@app_views.route('/users', methods=['GET'], strict_slashes=False)
@jwt_required()
def all_users():
    """ Retrieves all user objects """
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()]), 200

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_user(user_id):
    """ Retrieves a specific user """
    user = storage.get_by(User, id=user_id)

    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_user(user_id):
    """ Updates user profile """
    user = storage.get_by(User, id=user_id)

    if not user:
        abort(404)

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a valid JSON"}), 400

    ignore = ["id", "created_at", "updated_at", "email", "role"]

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()

    return jsonify({
        "message": "User profile updated successfully",
        "user": user.to_dict()
    }), 200

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_user(user_id):
    """ Deletes a user object that matches the user_id """
    user = storage.get_by(User, id=user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

@auth.route('/reset_password', methods=['POST'], strict_slashes=False)
@jwt_required()
def get_reset_password_token():
    """ Geerates reset password token """
    data = request.get_json()
    
    if not data:
        abort(400, description="Not a valid JSON")

    email = data.get('email')

    try:
        reset_token = auth_instance.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        }), 200
    except Exception:
        abort(403)

@auth.route('/reset_password', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_password():
    """ Update user password """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    email = data.get("email")
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")

    try:
        auth_instance.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)
