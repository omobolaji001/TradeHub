#!/usr/bin/env python3
"""Defines the Order model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(BaseModel, Base):
    """Represents an Order
    """
    __tablename__ = 'orders'

    customer_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Float, nullable=False, default=0.0)
    status = Column(String(20), nullable=False, default="Pending")


    shipment = relationship("Shipment", backref="order", uselist=False)
    items = relationship("OrderItem", backref="order")

    def __init__(self, *args, **kwargs):
        """ Initialize the order instance """
        super().__init__(*args, **kwargs)
