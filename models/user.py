#!/usr/bin/env python3
"""Defines the User class"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a User
    """
    __tablename__ = 'users'


    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    phone_number = Column(String(14), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    reset_token = Column(String(250), nullable=True)
    address = Column(String(500))
    role = Column(String(20), nullable=False, default='customer')


    orders = relationship("Order", backref="customer",
                          cascade="all, delete-orphan")
    cart = relationship("Cart", backref="customer",
                        cascade="all, delete-orphan")
    businesses = relationship("Business", backref="merchant")

    def __init__(self, *args, **kwargs):
        """ Initialize the User instance """
        super().__init__(*args, **kwargs)
