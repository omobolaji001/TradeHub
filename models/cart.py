#!/usr/bin/env python3
"""Defines the Cart model
"""
from models.base import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Cart(Base):
    """Represents a Cart
    """
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    items = relationship("CartItem", backref="cart",
                         cascade='all, delete-orphan', passive_deletes=True)
