#!/usr/bin/env python3
"""Defines Order item model
"""
from models.base import Base
from sqlalchemy import Column, Integer, Numeric, ForeignKey, DateTime
from datetime import datetime


class OrderItem(Base):
    """Represents an Order item
    """
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_item = Column(Numeric(precision=10, scale=2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    def to_dict(self):
        """ Dictionary representation of the Item """
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price_per_item": self.price_per_item,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
