#!/usr/bin/env python3
""" Routes for Product functionalities """
from models.product import Product
from models.merchant import Merchant
from models.engine.db import DB
from flask import request, abort, jsonify
from api.views import app_views
from api.v1.auth.utils import (
    authorize, token_required
)

db = DB()


@app_views('/products', methods=['POST'], strict_slashes=False)
@token_required
def register_product():
    """ Creates new product """
    user_id = g.user_id
    data = request.get_json()

    required_fields = ["name", "description", "price", "category_id"]

    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    merchant = Merchant.query.filter_by(user_id=user_id).first()
    if merchant:
        merchant_id = merchant.id

    try:
        # register new product
        new_product = Product(merchant_id=merchant_id, name=name,
                              category_id=category_id,
                              description=description, price=price)
        db.new(new_product)
        db.save()

    except Exception:
        return jsonify({"error": "Error while registering product!"}), 500


@app_views('/products', methods=['GET'], strict_slashes=False)
@token_required
def get_all_products():
    """ Retrieves all orders of a customer """
    try:
        products = db.all(Product)
        return jsonify([product.to_dict() for product in products]), 200
    except Exception:
        abort(404)


@app_views('/products/<int:product_id>', methods=['GET'], strict_slashes=False)
@token_required
def get_product(product_id):
    """ Retrieves a specific product """
    try:
        product = Product.query.filter_by(id=product_id).first()
        return jsonify(product.to_dict()), 200
    except Exception:
        abort(404)


@app_views('/products/<int:product_id>', methods=['PUT'], strict_slashes=False)
@token_required
def update_product(product_id):
    """ Update order """
    user_id = g.user_id
    merchant = Merchant.query.filter_by(user_id=user_id).first()
    merchant_id = merchant.id

    product = Product.query.filter_by(id=product_id,
                                      merchant_id=merchant_id).first()

    if not product:
        abort(404)

    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    ignore = ['created_at', 'updated_at', 'id', 'merchant_id', 'name']

    try:
        for key, value in data.items():
            if key not in ignore:
                setattr(product, key, value)
        db.save()
        
        return jsonify({
            "message": "Product updated successfully",
            "product": product.to_dict()
        }), 200
    except Exception:
        abort(500)


@app_views('/products/<int:product_id>', methods=['DELETE'], strict_slashes=False)
@token_required
def delete_product(product_id):
    """ Deletes a product from the database """
    user_id = g.user_id
    merchant = Merchant.query.filter_by(user_id=user_id).first()
    merchant_id = merchant.id

    try:
        product = Product.query.filter_by(id=product_id,
                                      merchant_id=merchant_id).first()
        db.delete(product)
        db.save()
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception:
        abort(404)
