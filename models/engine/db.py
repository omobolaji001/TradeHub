#!/usr/bin/env python3
""" Database Connection """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from dotenv import load_dotenv
from os import getenv
import models
from models.base import Base
from models.user import User
from models.business import Business
from models.product import Product
from models.order import Order
from models.cart import Cart
from models.category import Category
from models.order_item import OrderItem
from models.cart_item import CartItem
from models.payment import Payment

# load environment variables from .env file
load_dotenv()

classes = {
    "User": User, "Product": Product, "Business": Business,
    "Category": Category, "Order": Order, "Payment": Payment,
    "Cart": Cart, "OrderItem": OrderItem, "CartItem": CartItem
}


class DB:
    """Represents the Database class"""

    def __init__(self):
        """Initialize a new DB instance"""
        TRADEHUB_DB_USER = getenv("TRADEHUB_DB_USER")
        TRADEHUB_DB_PWD = getenv("TRADEHUB_DB_PWD")
        TRADEHUB_DB_HOST = getenv("TRADEHUB_DB_HOST")
        TRADEHUB_DB = getenv("TRADEHUB_DB")
        TRADEHUB_ENV = getenv("TRADEHUB_ENV")

        try:
            self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                         .format(TRADEHUB_DB_USER,
                                                 TRADEHUB_DB_PWD,
                                                 TRADEHUB_DB_HOST,
                                                 TRADEHUB_DB))
        except Exception as e:
            print("Error while connecting to the Database:", e)

        if TRADEHUB_ENV == "test":
            Beta.meatadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_one_commit=False)
        DBSession = scoped_session(sess_factory)
        self.__session = DBSession

        self.reload()

    def reload(self):
        """ Reloads data from the datababse """
        self.__session.remove()
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBSession = scoped_session(sess_factory)
        self.__session = DBSession


    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)


    def all(self, cls=None):
        """ Retrieves all objects of Merchant """
        new_dict = {}

        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                  key = obj.__class__.__name__  + '.' + obj.id
                  new_dict[key] = obj
        return new_dict

    def get_by(self, cls, **kwargs):
        """Finds object by key-word argument"""
        all_objs = models.storage.all(cls)

        for obj_key, obj in all_objs.items():
            if all(getattr(obj, key) == value for key, value in kwargs.items()):
                return obj

        return None

    def count(self, cls=None):
        """ Return the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).value())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def close(self):
        """Closes the current DB session"""
        self.__session.remove()
