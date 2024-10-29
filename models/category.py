#!/usr/bin/env python3
"""Defines the Category model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime


class Category(BaseModel, Base):
    """Represents a Category
    """
    __tablename__ = 'categories'

    name = Column(String(30), nullable=False)
    description = Column(Text, nullable=True)
    products = relationship("Product", backref="category")

    def __init__(*args, **kwargs):
        """ Initialize category instance """
        super().__init__(*args, **kwargs)
