#!/usr/bin/env python3
""" Merchant API endpoints """
from models.customer import Customer
from models.engine.db import DB
from api.v1.views import app_views
from api.v1.auth import auth
from api.v1.auth.utils import (
    token_required, authenticate,
    hash_password, generate_uuid
)
from flask import jsonify, request, abort, make_response

db = DB()


@auth.route('/register/customer', methods=['POST'], strict_slashes=False)
def register_customer():
    """ Creates a new customer object """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    required_fields = ['firstname', 'lastname', 'username', 'address',
                       'email', 'phone_number', 'password']

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

    try:
        user_id = db.add_user(role="Customer", **data)

        db.add_customer(user_id=user_id)

        return jsonify({"message": "Customer registered successfully!"}), 201
    except Exception:
        abort(500)

@app_views('/customers', methods=['GET'], strict_slashes=False)
def all_merchants():
    """ Retrieves all customer objects from the database """
    merchants = db.all(Customer)
    return jsonify([merchant.to_dict() for merchant in merchants]), 200

@app_views('/customers/<customer_id>', methods=['GET'], strict_slashes=False)
def get_merchant(customer_id):
    """ Retrieves a specific customer """
    customer = db.get(Customer, customer_id)

    if not customer:
        abort(404)
    return jsonify(customer.to_dict()), 204

@app_views('/customers/<customer_id>', methods=['PUT'], strict_slashes=False)
def update_merchant(customer_id):
    """ Updates a customer object that matches the customer_id """
    customer = db.get(Customer, customer_id)

    if not customer:
        abort(404)

    user_id = customer.user_id

    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    db.update_user(user_id, **data)
    return jsonify({"message": "Merchant updated successfully"}), 200

@app_views('/customers/<customer_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_merchant(customer_id):
    """ Deletes a customer object that matches the customer_id """
    customer = db.get(Customer, customer_id)

    if not customer:
        abort(404)

    db.delete(customer)
    db.save()

    return make_response(jsonify({}), 204)
