#!/usr/bin/env python3
"""Defines the User class"""
from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    """Represents a User
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    hashed_password = Column(String(120), nullable=False)
    reset_token = Column(String(250), nullable=True)
    is_merchant = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
