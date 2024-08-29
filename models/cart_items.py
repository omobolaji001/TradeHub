#!/usr/bin/env python3
"""Defines Cart item model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey


class CartItem(BaseModel):
    """Represents a Cart item
    """
    __tablename__ = 'cart_items'

    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
