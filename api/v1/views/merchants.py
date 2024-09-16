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

    required_fields = ['firstname', 'lastname', 'username',
                       'email', 'password',
                       'business_name', 'business_description']

    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400)

    hashed_password = hash_password(data.get('password'))
    fname = data.get('firstname')
    lname = data.get('lastname')
    uname = data.get('username')
    email = data.get('email')
    role = 'Merchant'
    b_name = data.get('business_name')
    b_description = data.get('business_description')

    try:
        user_id = db.add_user(firstname=fname, lastname=lname, username=uname,
                              email=email, role=role)
        db.add_merchant(user_id=user_id, business_name=b_name,
                        business_description=b_description)
        return jsonify({"message": "Merchant registered successfully!"}), 201
    except ValueError:
        return jsonify({"error": "merchant already registered!"}), 400

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
    return jsonify(merchant.to_dict())

@app_views('/merchants/<merchant_id>', methods=['PUT'], strict_slashes=False)
def update_merchant(merchant_id):
    """ Updates a merchant object that matches the merchant_id """
    merchant = db.get(Merchant, merchant_id)

    if not merchant:
        abort(404)

    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    ignore = [
                'id', 'email', 'created_at', 'updated_at',
                'firstname', 'lastname', 'role'
    ]

    for key, value in data.items():
        if key not in ignore:
            setattr(merchant, key, value)
    db.save()
    return make_response(jsonify(merchant.to_dict()), 200)
