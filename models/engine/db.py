#!/usr/bin/env python3
"""Defines the Database connection
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from models.user import User
from models.product import Product
from models.order import Order
from models.cart import Cart
from models.category import Category
from models.order_item import OrderItem
from models.cart_item import CartItem


TRADEHUB_DB_USER = getenv("TRADEHUB_DB_USER")
TRADEHUB_DB_PWD = getenv("TRADEHUB_DB_PASSWORD")
TRADEHUB_DB_HOST = getenv("TRADEHUB_DB_HOST")
TRADEHUB_DB_PORT = getenv("TRADEHUB_DB_PORT")
TRADEHUB_DB = getenv("TRADEHUB_DB")


class DB:
    """Represents the Database class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(
                                     TRADEHUB_DB_USER, TRADEHUB_DB_PWD,
                                     TRADEHUB_DB_HOST, TRADEHUB_DB_PORT,
                                     TRADEHUB_DB))
