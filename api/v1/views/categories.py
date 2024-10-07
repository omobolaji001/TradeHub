#!/usr/bin/env python3
""" Routes for Category functionalities """
from models.category import Category
from models import db
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from api.v1.auth.utils import (
    authenticate, token_required
)


@app_views('/categories', methods=['POST'], strict_slashes=False)
def create_category():
    """ Creates a new category for products """
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    name = data.get("name")

    if not name:
        abort(400, description="name is required to create a category")

    existing = Category.query.filter_by(name=name)
    if existing:
        return jsonify({"error": "Category already exists"}), 409

    try:
        category = Category(name=name)
        db.new(category)
        db.save()
        return jsonify({"message": "Category created successfully!"}), 201
    except Exception:
        abort(500)

@app_views('/categories', methods=['GET'], strict_slashes=False)
def get_all_categories():
    """ Retrieves all product categories """
    try:
        categories = db.all(Category)
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception:
        abort(500)


@app_views('/categories/<int:category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """ Retrieves a category that matches the category ID """
    try:
        category = Category.query.filter_by(id=category_id).first()
        return jsonify(category.to_dict()), 200
    except Exception:
        abort(404)


@app_views('/categories/<int:category_id>', methods=['PUT'], strict_slashes=False)
def rename_category(category_id):
    """ Renames an existing category """
    data = request.get_json()
    if not data:
        abort(400, description="Not a valid JSON")

    name = data.get("name")
    if not name:
        abort(400, description="name attribute is required")

    try:
        category = Category.query.filter_by(idcaegory_id).first()
        category.name = name
        db.save()
        return jsonify({"message": "Category name updated successfully!"}), 200
    except Exception:
        abort(404)


@app_views('/categories/<int:category_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_category(category_id):
    """ Deletes a category """
    try:
        category = Category.query.filter_by(id=category_id)
        db.delete(category)
        db.save()
        return make_response('', 204)
    except Exception:
        abort(404)
