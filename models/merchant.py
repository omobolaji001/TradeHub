#!/usr/bin/env python3
"""Defines the Merchant class"""
from models.base import Base
from sqlalchemy import Column, String, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Merchant(Base):
    """Represents a Merchant
    """
    __tablename__ = 'merchants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    business_name = Column(String(250), unique=True, nullable=False)
    business_description = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())
