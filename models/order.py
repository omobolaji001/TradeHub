#!/usr/bin/env python3
"""Defines the Order model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, DateTime, Numeric, String, ForeignKey
from datetime import datetime


class Order(BaseModel):
    """Represents an Order
    """
    __tablename__ = 'orders'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Numeric(precision=12, scale=2), nullable=False)
    status = Column(String(30))
