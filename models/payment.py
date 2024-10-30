#!/usr/bin/env python3
"""Defines the Payment model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Numeric, ForeignKey
from datetime import datetime


class Payment(BaseModel, Base):
    """Payment class
    """

    __tablename__ = 'payments'

    order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    payment_method = Column(String(50))
    payment_status = Column(String(50), default='pending')

    def __init__(self, *args, **kwargs):
        """ Initialize paymnet instances """
        super().__init__(*args, **kwargs)
