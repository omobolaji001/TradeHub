#!/usr/bin/env python3
""" Merchant API endpoints """
from models.merchant import Merchant
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


@auth.route('/register/merchant', methods=['POST'], strict_slashes=False)
def register_merchant():
    """ Creates a new Merchant object """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    required_fields = ['firstname', 'lastname', 'username', 'address',
                       'email', 'phone_number', 'password',
                       'business_name', 'business_description']

    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400)

    existing_mail = db.find_user_by(email=data.get("email"))
    if existing_mail:
        abort(409, description="User with this email already exists")

    existing_username = db.find_user_by(username=data.get("username"))
    if existing_username:
        abort(409, description="username already exists")

    data["password"] = hash_password(data.get("password"))

    business_name = data.pop("business_name")
    business_description = data.pop("business_description")

    try:
        user_id = db.add_user(role="Merchant", **data)

        db.add_merchant(user_id=user_id, business_name=b_name,
                        business_description=b_description)

        return jsonify({"message": "Merchant registered successfully!"}), 201
    except Exception:
        abort(500)

@app_views('/merchants', methods=['GET'], strict_slashes=False)
def all_merchants():
    """ Retrieves all merchant objects """
    merchants = db.all(Merchant)
    return jsonify([merchant.to_dict() for merchant in merchants]), 200

@app_views('/merchants/<merchant_id>', methods=['GET'], strict_slashes=False)
def get_merchant(merchant_id):
    """ Retrieves a specific merchant """
    merchant = db.get(Merchant, merchant_id)

    if not merchant:
        abort(404)
    return jsonify(merchant.to_dict()), 204

@app_views('/merchants/<merchant_id>', methods=['PUT'], strict_slashes=False)
def update_merchant(merchant_id):
    """ Updates a merchant object that matches the merchant_id """
    merchant = db.get(Merchant, merchant_id)

    if not merchant:
        abort(404)

    user_id = merchant.user_id

    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    if business_name and business_description in data.keys():
        b_name = data.pop("business_name")
        b_descr = data.pop("business_description")
        setattr(merchant, business_name=b_name, business_description=b_descr)

    db.update_user(user_id, **data)
    db.save()
    return jsonify({"message": "Merchant updated successfully"}), 200

@app_views('/merchants/<merchant_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_merchant(merchant_id):
    """ Deletes a merchat object that matches the merchant_id """
    merchant = db.get(Merchant, merchant_id)

    if not merchant:
        abort(404)

    db.delete(merchant)
    db.save()

    return make_response(jsonify({}), 204)
