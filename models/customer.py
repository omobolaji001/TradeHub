#!/usr/bin/env python3
"""Defines the Customer class"""
from models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from datetime import datetime

class Customer(Base):
    """Represents a Customer
    """
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    phone_number = Column(String(14), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
