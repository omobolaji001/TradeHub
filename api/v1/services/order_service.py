#!/usr/bin/env python3
""" Order service """
from models.order import Order
from models.cart import Cart 
from models import storage
from models.product import Product
from models.order_item import OrderItem
from api.v1.services.shipment_service import create_shipment
# from api.v1.services import process_payment


def process_checkout(user_id, shipping_address, shipping_cost, date):
    """ Handles checkout """
    cart = storage.get_by(Cart, user_id=user_id)
    if not cart or len(cart.items) == 0:
        raise Exception("Cart is empty")

    total_amount = 0.00
    order_items = []
    for item in cart.items:
        product = storage.get_by(id=item.product_id)
        if product.stock < item.quantity:
            raise Exception(f"Insufficient stock for product {product.name}")
            
        total_amount += item.quatity * product.price

    # create order
    order = Order(customer_id=user_id, total_amount=total_amount, order_date=date)
    order.save()

    # create order items and deduct stocks
    for item in cart.items:
        product = storage.get_by(id=item.product_id)
        product.stock -= item.quantity
        product.save()

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price
        )

        order_item.save()

    # clear cart
    storage.delete(cart)

    # process payment
    """payment = process_payment(order, user_id)

    if payment == "success":
        order.status = "completed"
    else:
        order.status = "payment failed"
    """

    shipment = create_shipment(order, shipping_address, shipping_cost)

    storage.save()

    return {
        "message": "Order created successfully",
        "order_id": new_order.id,
        "shipment_id": shipment.id,
        "total_amount": order.total_amount
    }
