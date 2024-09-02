#!/usr/bin/env python3
"""Defines the Database connection
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
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

Base = declarative_base()
classes = {
            "User": User, "Product": Product,
            "Category": Caegory, "Order": Order,
            "Cart": Cart, "OrderItem": OrderItem,
            "CartItem": CartItem
}


class DB:
    """Represents the Database class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        try:
            self._engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(
                                         TRADEHUB_DB_USER, TRADEHUB_DB_PWD,
                                         TRADEHUB_DB_HOST, TRADEHUB_DB_PORT,
                                         TRADEHUB_DB))
        except Exception as e:
            print("Error while connecting to the Database": e)

        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Represents a Memoized session object
        """
        if self.__session is None:
            session_factory = sessionmaker(bind=self._engine)
            DBSession = scoped_session(session_factory)
            self.__session = DBSession()
        return self.__session

    def all(self, cls=None):
        """Retrieves all objects of a class
        """
        new = {}
        for clss in classes:
            if cls is None or cls is classes[clss] of cls is clss:
                objs = self._session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new[key] = obj
        return new

    def new(self, obj):
        """Adds the object to the current database session
        """
        self._session.add(obj)

    def save(self):
        """Commits all changes to the database
        """
        self._session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session
        """
        if obj is not None:
            self._session.delete(obj)

    def get(self, cls, id):
        """Retrieves an object from the database by id
        """
        if cls is not None and id is not None:
            obj = self._session.query(cls).get(id)
            return obj
        return None

    def get_by_email(self, cls, email):
        """Retrieves object from the database by email
        """
        if cls is not None and email is not None:
            obj = self._session.query(cls).filter_by(email=email).first()
            return obj
        return None

    def close(self):
        """Closes the current DB session
        """
        self._session.remove()
