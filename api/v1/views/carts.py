#!/usr/bin/env python3
""" Routes for order functionalities """
from models.cart import Cart
from models.cart_item import CartItem
from models.user import User
from models import storage
from flask import request, abort, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.v1.views import app_views
from api.v1.auth.utils import authorize


@app_views.route('/cart/items', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_item_to_cart():
    """ Adds new item to cart """
    user_id = get_jwt_identity()

    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a valid JSON"}), 400

    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    cart = storage.get_by(Cart, customer_id=user_id)
    if not cart:
        cart = Cart(customer_id=user_id)
        cart.save()

    cart_item = storage.get_by(cart_id=cart.id, product_id=product_id)
    if cart_item:
        # Update the quantity if item already exists
        cart_item.quantity += quantity
    else:
        # Add the item to cart
        new_cart_item = CartItem(cart_id=cart.id, product_id=product_id,
                                 quantity=quantity)
        storage.new(new_cart_item)

    # Commit changes to database
    storage.save()

    return jsonify({"message": "Item added to cart successfully"}), 201

    
@app_views.route('/cart', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_cart_items():
    """ Retrieves all items in a cart """
    user_id = get_jwt_identity()

    cart = storage.get_by(Cart, customer_id=user_id)
    if not cart:
        return jsonify({"message": "Cart is empty"}), 200

    try:
        items = cart.items
        total_price = sum(item.product.price * item.quantity for item in items)
        return jsonify({
            "cart_items": [item.to_dict() for item in items],
            "total_price": total_price
        }), 200
    except Exception:
        abort(500)


@app_views.route('/cart/items/<item_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_cart_item(item_id):
    """ Update the quantity of a cart item """
    user_id = get_jwt_identity()

    data = request.get_json()
    quantity = data.get("quantity")

    if quantity is None or quantity <= 0:
        return jsonify({"error": "Invalid quantity"}), 400

    cart = storage.get_by(Cart, customer_id=user_id)

    for item in cart.items:
        if item.id == item_id:
            item.quantity = quantity
            item.save()
        
            return jsonify({
                "message": "Cart item updated successfully",
                "item": item.to_dict()
            }), 200

    return jsonify({"error": "Item not found"}), 404


@app_views.route('/cart/items/<item_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def remove_cart_item(item_id):
    """ Remove an item from cart """
    user_id = get_jwt_identity()

    cart = storage.get_by(Cart, customer_id=user_id)

    for item in cart.items:
        if item.id == item_id:
            storage.delete(item)
            storage.save()

            return jsonify({"message": "Item removed successfully"}), 200

    return jsonify({"error": "Item not found"}), 404


@app_views.route('/cart/clear', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def clear_cart():
    """ Removes all items from cart """
    user_id = get_jwt_identity()

    cart = storage.get_by(Cart, customer_id=user_id)

    if not cart:
        return jsonify({"message": "Cart is already empty"}), 200

    for item in cart.items:
        storage.delete(item)
    storage.save()

    return jsonify({"message": "Cart cleared successfully"}), 200
