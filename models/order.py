#!/usr/bin/env python3
"""Defines the Order model
"""
from models.base import Base
from sqlalchemy import Column, Integer, DateTime, Numeric, String, ForeignKey
from datetime import datetime


class Order(Base):
    """Represents an Order
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Numeric(12, 2), nullable=False)
    status = Column(String(30), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
