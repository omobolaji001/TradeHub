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
    phone_number = Column(String(14), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    address = Column(String(600), nullable=False)
    hashed_password = Column(String(120), nullable=False)
    reset_token = Column(String(250), nullable=True)
    role = Column(String(100), nullable=False, default='Customer')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow())

    merchant = relationship('Merchant', backref='user', cascade='all, delete',
                            uselist=False, passive_deletes=True)
    customer = relationship('Customer', backref='user', cascade='all, delete',
                            uselist=False, passive_deletes=True)

    def to_dict(self):
        """ Returns the instance in dictionary form """
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "role": self.role,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
