#!/usr/bin/env python3
"""Defines the Product model
"""
from models.base import Base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from datetime import datetime


class Product(Base):
    """Represents a Product
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    merchant_id = Column(Integer, ForeignKey('merchants.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(60))
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    image_url = Column(String(30), nullable=False, default='default.jpg')
    category_id = Column(Integer, ForeignKey('categories.id',
                         ondelete='SET NULL'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
