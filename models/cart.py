#!/usr/bin/env python3
"""Defines the Cart model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Cart(BaseModel):
    """Represents a Cart
    """
    __tablename__ = 'carts'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    items = relationship("CartItem", backref="cart")
