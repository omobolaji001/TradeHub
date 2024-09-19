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
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    business_name = Column(String(250), unique=True, nullable=False)
    business_description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    def to_dict(self):
        """ Returns dictionary of instance """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "business_name": self.business_name,
            "business_description": self.business_description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
