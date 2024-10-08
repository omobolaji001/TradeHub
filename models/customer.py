#!/usr/bin/env python3
"""Defines the Customer class"""
from models.base import Base
from sqlalchemy import (
    Column, String, Integer,
    ForeignKey, DateTime
)
from sqlalchemy.orm import relationship
from datetime import datetime

class Customer(Base):
    """Represents a Customer
    """
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    orders = relationship('Order', backref='customer',
                          cascade='all, delete, delete-orphan')

    def to_dict(self):
        """ Returns User data in dictionary format """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
