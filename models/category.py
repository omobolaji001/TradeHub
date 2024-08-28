#!/usr/bin/env python3
"""Defines the Category model
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Category(BaseModel):
    """Represents a Category
    """
    __tablename__ = 'categories'

    name = Column(String(30))
