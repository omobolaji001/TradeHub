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
    price = Column(Numeric(precision=10, scale=2), nullable=False,
                   default=0.00)
    image_url = Column(String(30), nullable=False, default='default.jpg')
    category_id = Column(Integer, ForeignKey('categories.id'),
                         nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    def to_dict(self):
        """ Dictionary representation of object """
        return {
            "id": self.id,
            "merchant_id": self.merchant_id,
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
