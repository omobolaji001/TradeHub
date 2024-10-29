#!/usr/bin/env python3
"""Defines the Cart model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Cart(BaseModel, Base):
    """Represents a Cart
    """
    __tablename__ = 'carts'

    customer_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    total_amount = Column(Float, default=0.0)

    items = relationship("CartItem", backref="cart",
                         cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """ Initializes the cart instance """
        super().__init__(*args, **kwargs)
