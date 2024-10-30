#!/usr/bin/env python3
""" Routes for order functionalities """
from models.order import Order
from models.order_item import OrderItem
from models import storage
from models.user import User
from flask import request, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.v1.views import app_views
from api.v1.auth.utils import authorize
from api.v1.services import process_checkout


@app_views.route('/checkout', methods=['POST'], strict_slashes=False)
@jwt_required()
def checkout():
    """ Creates new order """
    user_id = get_jwt_identity()

    data = request.get_json()

    shipping_address = data.get("shipping_address")
    shipping_cost = data.get("shipping_cost")
    date = data.get("order_date")
    
    if not shipping_address or not all(key in shipping_address for key in ('street', 'city', 'state', 'zip_code')):
        return jsonify({"error": "Invalid shipping address"}), 400

    try:
        result = process_checkout(user_id, shipping_address, shipping_cost, date)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app_views.route('/orders', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_orders():
    """ Retrieves all orders of a customer """
    user_id = get_jwt_identity()

    user = storage.get_by(User, id=user_id)

    try:
        orders = user.orders
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception:
        abort(404, description="No orders found for this user")


@app_views.route('/orders/<order_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_order(order_id):
    """ Retrieves a specific order """
    user_id = get_jwt_identity()

    try:
        order = storage.get_by(Order, id=order_id, customer_id=user_id)
        return jsonify(order.to_dict()), 200
    except Exception:
        abort(404)


@app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_order(order_id):
    """ Update order status"""
    data = request.get_json()
    new_status = data.get("status")

    valid_status = ["Pending", "Confirmed", "Shipped", "Canceled", "Delivered"]
    if new_status not in valid_status:
        return jsonify({"error": "Invalid order status"}), 400

    user_id = get_jwt_identity()

    try:
        order = storage.get_by(Order, id=order_id, customer_id=user_id)
        order.status = new_status
        order.save()

        return jsonify({
            "message": f"Order status updated to {new_status}",
            "order": order.to_dict()
        }), 200
    except Exception:
        abort(404)


@app_views.route('/orders/<order_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def cancel_order(order_id):
    """ Cancles an order """
    user_id = get_jwt_identity()

    try:
        order = storage.get_by(Order, id=order_id, customer_id=user_id)
        storage.delete(order)
        storage.save()
        return jsonify({"message": "Order cancelled successfully"}), 200
    except Exception:
        abort(404)

@app_views.route('/shipments/<order_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_shipment(order_id):
    """ Retrieve Shipment information """
    user_id = get_jwt_identity()

    order = storage.get_by(Order, customer_id=user_id, id=order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if not order.shipment:
        return jsonify({"error": "Shipment not found"}), 404

    shipment = order.shipment
    return jsonify(shipment.to_dict()), 200

@app_views.route('/shipments/<order_id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_shipment_status(order_id):
    """ Updates shipment status """
    user_id = get_jwt_identity()

    order = storage.get_by(Order, id=order_id, customer_id=user_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    shipment = order.shipment
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404

    valid_status = ["Pending", "Shipped", "Delivered"]

    data = request.get_json()
    new_status = data.get("status")
    tracking_number = data.get("tracking_number")

    # Validate input
    if not new_status or not tracking_number:
        return jsonify({"error": "Missing status or tracking number"}), 400

    if new_status not in valid_status:
        return jsonify({"error": f"Invalid shipment status"}), 404

    shipment.status = new_status
    shipment.tracking_number = tracking_number
    shipment.save()

    return jsonify({
        "message": "Shipment status updated successfully",
        "shipment_id": shipment.id,
        "status": shipment.status,
        "tracking_number": shipment.tracking_number
    }), 200
