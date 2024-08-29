#!/usr/bin/env python3
"""Defines Order item model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class OrderItem(BaseModel):
    """Represents an Order item
    """
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
