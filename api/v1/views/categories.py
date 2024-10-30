#!/usr/bin/env python3
""" Routes for Category functionalities """
from models.category import Category
from models import storage
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from api.v1.auth.utils import authorize
from flask_jwt_extended import jwt_required


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
@jwt_required()
def create_category():
    """ Creates a new category for products """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a valid JSON"}), 400

    name = data.get("name")
    description = data.get("description", None)

    if not name:
        return jsonify({"error": "name is required to create a category"}), 400

    existing = storage.get_by(Category, name=name, description=description)
    if existing:
        return jsonify({"error": "Category already exists"}), 409

    try:
        category = Category(name=name)
        category.save()

        return jsonify({"message": "Category created successfully!"}), 201
    except Exception:
        abort(500)

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_all_categories():
    """ Retrieves all product categories """
    try:
        categories = storage.all(Category)
        return jsonify([category.to_dict() for category in categories.values()]), 200
    except Exception:
        abort(500)


@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """ Retrieves a category that matches the category ID """
    category = storage.get_by(Category, id=category_id)

    if not category:
        abort(404)
    
    return jsonify(category.to_dict()), 200


@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)
def update_category(category_id):
    """ Updates an existing category """
    data = request.get_json()
    if not data:
        abort(400, description="Not a valid JSON")

    name = data.get("name")
    description = data.get("description")

    category = storage.get_by(Category, id=category_id)
    
    if category:
        if name:
            category.name = name
        if description:
            category.description = deescription
        category.save()

        return jsonify({"message": "Category name updated successfully!"}), 200
    else:
        abort(404)
    

@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """ Deletes a category """
    category = storage.get_by(Category, id=category_id)
    if not category:
        abort(404)

    storage.delete(category)
    storage.save()

    return jsonify({"message": "Category removed successfully"}), 200
