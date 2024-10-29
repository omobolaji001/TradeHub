#!/usr/bin/env python3
"""Defines Order item model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from datetime import datetime


class OrderItem(BaseModel, Base):
    """Represents an Order item
    """
    __tablename__ = 'order_items'

    order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False, default=0.0)

    def __init__(self, *args, **kwargs):
        """ Initialize order_item instance """
        super().__init__(*args, **kwargs)
