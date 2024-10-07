#!/usr/bin/env python3
""" Routes for order functionalities """
from models.cart import Cart
from models.cart_item import CartItem
from models.customer import Customer
from models import db
from flask import request, abort, jsonify
from api.views import app_views
from api.v1.auth.utils import (
    authorize, token_required
)


@app_views('/cart/items', methods=['POST'], strict_slashes=False)
@token_required
def add_item_to_cart():
    """ Adds new item to cart """
    user_id = g.user_id
    data = request.get_json()

    if not data:
        abort(400, description="Not a valid JSON")

    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    customer = Customer.query.filter_by(user_id=user_id).first()
    if customer:
        customer_id = customer.id

    cart = Cart.query.filter_by(customer_id=customer_id).first()
    if not cart:
        cart = Cart(customer_id=customer_id)
        db.new(cart)
        db.save()

    cart_itemn = CartItem.query.filter_by(cart_id=cart.id,
                                          product_id=product_id).first()
    if cart_item:
        # Update the quantity if item already exists
        cart_item.quantity += quantity
    else:
        # Add the item to cart
        new_cart_item = CartItem(cart_id=cart.id, product_id=product_id,
                                 quantity=quantity)
        db.new(new_cart_item)

    # Commit changes to database
    db.save()

    return jsonify({"message": "Item added to cart successfully"}), 201

    
@app_views('/cart', methods=['GET'], strict_slashes=False)
@token_required
def get_cart_items():
    """ Retrieves all items in a cart """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()

    cart = Cart.query.filter_by(customer_id=customer.id).first()
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


@app_views('/cart/items/<int:item_id>', methods=['PUT'], strict_slashes=False)
@token_required
def update_cart_item(item_id):
    """ Update the quantity of a cart item """
    data = request.get_json()
    quantity = data.get("quantity")

    if not quantity or quantity <= 0:
        return jsonify({"error": "Invalid quantity"}), 400

    user_id = g.user_id
    customer = Cutomer.query.filter_by(user_id=user_id).first()
    customer_id = customer.id

    cart_item = CartItem.query.join(Cart).filter(CartItem.id==item_id,
                                                 Cart.customer_id==customer_id).first()
    if not cart_item:
        abort(404)

    cart_item.quantity = quantity
    db.save()
        
    return jsonify({
        "message": "Cart item updated successfully",
        "item": cart_item.to_dict()
    }), 200


@app_views('/cart/items/<int:item_id>', methods=['DELETE'], strict_slashes=False)
@token_required
def remove_cart_item(item_id):
    """ Remove an item from cart """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()
    customer_id = customer.id

    cart_item = CartItem.query.join(Cart).filter(CartItem.id==item_id,
                                                 Cart.customer_id==customer_id).first()
    if not cart_item:
        abort(404)

    db.delete(cart_item)
    db.save()
    
    return jsonify({"message": "Item removed successfully"}), 200


@app_views('/cart/clear', methods=['DELETE'], strict_slashes=False)
@token_required
def clear_cart():
    """ Removes all items from cart """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()

    cart = Cart.query.filter_by(customer_id=customer.id).first()
    if not cart:
        return jsonify({"message": "Cart is already empty"}), 200

    CartItem.query.filter_by(cart_id=cart.id).delete()
    db.save()

    return jsonify({"message": "Cart cleared successfully"}), 200
