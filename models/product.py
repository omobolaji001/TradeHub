#!/usr/bin/env python3
"""Defines the Product model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey


class Product(BaseModel, Base):
    """Represents a Product
    """
    __tablename__ = 'products'

    business_id = Column(String(60), ForeignKey('businesses.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialize product instance """
        super().__init__(*args, **kwargs)
