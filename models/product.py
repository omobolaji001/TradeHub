#!/usr/bin/env python3
"""Defines the Product model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey


class Product(BaseModel):
    """Represents a Product
    """
    __tablename__ = 'products'

    name = Column(String(60), nullable=False)
    description = Column(String(60))
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    image_url = Column(String(30), nullable=False, default='default.jpg')
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
