#!/usr/bin/env python3
""" Shipping service
"""
from models.shipment import Shipment
from models import storage

def create_shipment(order, shipping_address, shipping_cost):
    """ Creates shipment instance for the order
    """
    shipment = Shipment(
        order_id=order.id,
        shipping_address=f"{shipping_address['street']}, {shipping_address['city']}, {shipping_address['state']}, {shipping_address['zip_code']}",
        status="Processing",
        shipping_cost=shipping_cost,
        tracking_number=None
    )
    shipment.save()

    return shipment
