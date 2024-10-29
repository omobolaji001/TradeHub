#!/usr/bin/env python3
"""Defines Cart item model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class CartItem(BaseModel, Base):
    """Represents a Cart item
    """
    __tablename__ = 'cart_items'

    cart_id = Column(String(60), ForeignKey('carts.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialize the instance """
        super().__init__(*args, **kwargs)
