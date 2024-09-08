#!/usr/bin/env python3
"""Defines Cart item model
"""
from models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime


class CartItem(Base):
    """Represents a Cart item
    """
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id', ondelete='CASCADE'),
                     nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
