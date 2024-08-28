#!/usr/bin/env python3
"""Defines the User class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, Boolean


class User(BaseModel):
    """Represents a User
    """
    __tablename__ = 'users'

    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    username = Column(String(30), unique=True, nllable=False)
    password = Column(String(120), nullable=False)
    is_merchant = Column(Boolean, default=False)
