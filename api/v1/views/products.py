#!/usr/bin/env python3
""" Routes for Product functionalities """
from models.product import Product
from models import storage
from flask import request, abort, jsonify
from api.v1.views import app_views
from api.v1.auth.utils import authorize
from flask_jwt_extended import get_jwt_identity, jwt_required


@app_views.route('/products', methods=['POST'], strict_slashes=False)
@jwt_required()
def register_product():
    """ Creates new product """
    user_id = get_jwt_identity()

    data = request.get_json()

    required_fields = ["name", "description", "price", "category_id"]

    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        # register new product
        new_product = Product(user_id=user_id, **data)
        new_product.save()

    except Exception:
        return jsonify({"error": "Error while registering product!"}), 500


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_all_products():
    """ Retrieves all orders of a customer """
    try:
        products = storage.all(Product)
        return jsonify([prdt.to_dict() for prdt in products.values()]), 200
    except Exception:
        abort(404)


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
    """ Retrieves a specific product """
    try:
        product = storage.get_by(Product, id=product_id)
        return jsonify(product.to_dict()), 200
    except Exception:
        abort(404)


@app_views.route('/products/<product_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_product(product_id):
    """ Update order """
    user_id = get_jwt_identity()

    product = storage.get_by(Product, id=product_id, user_id=user_id)

    if not product:
        abort(404)

    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    ignore = ['created_at', 'updated_at', 'id', 'user_id']

    try:
        for key, value in data.items():
            if key not in ignore:
                setattr(product, key, value)
        product.save()
        
        return jsonify({
            "message": "Product updated successfully",
            "product": product.to_dict()
        }), 200
    except Exception:
        abort(500)


@app_views.route('/products/<product_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_product(product_id):
    """ Deletes a product from the database """
    user_id = get_jwt_identity()

    try:
        product = storage.get_by(Product, id=product_id, user_id=user_id)
        storage.delete(product)
        storage.save()

        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception:
        abort(404)
