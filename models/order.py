#!/usr/bin/env python3
"""Defines the Order model
"""
from models.base import Base
from sqlalchemy import (
    Column, Integer, DateTime, Numeric,
    String, ForeignKey, relationship
)
from datetime import datetime


class Order(Base):
    """Represents an Order
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Numeric(12, 2), nullable=False, default=0.00)
    shipping_address = Column(String(300), nullable=False)
    status = Column(String(30), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    items = relationship("OrderItem", backref="order")

    def to_dict(self):
        """ Returns a dictionary representation of the object """
        return {
            "id": self.id,
            "user_id": self.id,
            "order_date": self.order_date,
            "total_amount": self.total_amount,
            "shipping_address": self.shipping_address,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
