#!/usr/bin/env python3
"""Defines the Category model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Category(BaseModel):
    """Represents a Category
    """
    __tablename__ = 'categories'

    name = Column(String(30))

    products = relationship("Product", backref="category")
