#!/usr/bin/env python3
""" Routes for order functionalities """
from models.order import Order
from models.order_item import OrderItem
from models.customer import Customer
from models.engine.db import DB
from flask import request, abort, jsonify
from api.views import app_views
from api.v1.auth.utils import (
    authorize, token_required
)
from api.v1.views.helper import get_product_price

db = DB()


@app_views('/orders', methods=['GET'], strict_slashes=False)
@token_required
def create_order():
    """ Creates new order """
    user_id = g.user_id
    data = request.get_json()
    items = data.get("items")
    shipping_address = data.get("shipping_address")

    if not shipping_address or not items:
        return jsonify({"error": "Shipping address and items are required"}), 400

    customer = Customer.query.filter_by(user_id=user_id).first()
    if customer:
        customer_id = customer.id

    try:
        # Create new order in the database
        new_order = Order(customer_id=customer_id)
        db.new(new_order)

        # Save the new order temporarily without commiting to database
        # to get the order id
        db.flush()
    except Exception:
        return jsonify({"error": "Error while creating order"}), 500

    total_amount = 0.00
    order_items = []
    for item in items:
        product_id = item.get("product_id")
        quantity = item.get("quantity", 1)

        if not product_id or quantity <= 0:
            return jsonify({"error": "Invalid product ID or quantity"}), 400

        # Get the price of the product
        price_per_item = get_product_price(product_id)

        if price_per_item is None:
            return jsonify({"error": f"No product with product ID {product_id} is found"}), 404

        # Calculate the total amount of the order
        total_amount += price_per_item * quantity

        # Create an OrderItem object
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=product_id,
            quantity=quantity,
            price_per_item=price_per_item
        )

        db.new(order_item)
        order_items.append(order_item)

    # Update the total amount of the new order created
    new_order.total_amount = total_amount

    # Commit changes to database
    db.save()

    return jsonify({
        "message": "Order created successfully",
        "order_id": new_order.id,
        "total_amount": new_order.total_amount,
        "order_items": [item.to_dict() for item in order_items]
    }), 201

    
@app_views('/orders', methods=['GET'], strict_slashes=False)
@token_required
def get_orders():
    """ Retrieves all orders of a customer """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()

    try:
        orders = customer.orders
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception:
        abort(404)


@app_views('/orders/<order_id>', methods=['GET'], strict_slashes=False)
@token_required
def get_order(order_id):
    """ Retrieves a specific order """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()
    customer_id = customer.id

    try:
        order = Order.query.filter_by(id=order_id,
                                      customer_id=customer_id).first()
        return jsonify(order.to_dict()), 200
    except Exception:
        abort(404)


@app_views('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
@token_required
def update_order(order_id):
    """ Update order """
    data = request.get_json()
    new_status = data.get("status")

    if not new_status:
        return jsonify({"error": "Order status is required"}), 400

    user_id = g.user_id
    customer = Cutomer.query.filter_by(user_id=user_id).first()
    customer_id = customer.id

    try:
        order = Order.query.filter_by(id=order_id,
                                      customer_id=customer_id).first()
        order.status = new_status
        db.save()
        
        return jsonify({
            "message": "Order status updated successfully",
            "order": order.to_dict()
        }), 200
    except Exception:
        abort(404)


@app_views('/orders/<order_id>', methods=['DELETE'], strict_slashes=False)
@token_required
def cancel_order(order_id):
    """ Cancles an order """
    user_id = g.user_id
    customer = Customer.query.filter_by(user_id=user_id).first()
    customer_id = customer.id

    try:
        order = Order.query.filter_by(id=order_id,
                                      customer_id=customer_id).first()
        db.delete(order)
        db.save()
        return jsonify({"message": "Order cancelled successfully"}), 200
    except Exception:
        abort(404)
