#!/usr/bin/env python3
"""Defines the Payment model
"""
from models.base import Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from datetime import datetime


class Payment(Base):
    """Payment class
    """

    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    payment_method = Column(String(50))
    payment_status = Column(String(50), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
