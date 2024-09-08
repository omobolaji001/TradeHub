#!/usr/bin/env python3
""" Database Connection """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from dotenv import load_dotenv
from os import getenv
from models.base import Base
from models.user import User
from models.product import Product
from models.order import Order
from models.cart import Cart
from models.category import Category
from models.order_item import OrderItem
from models.cart_item import CartItem
from models.merchant import Merchant
from models.customer import Customer
from models.payment import Payment

load_dotenv()
classes = {
    "User": User, "Product": Product, "Customer": Customer,
    "Category": Category, "Order": Order, "Payment": Payment,
    "Cart": Cart, "OrderItem": OrderItem,
    "CartItem": CartItem, "Merchant": Merchant
}


class DB:
    """Represents the Database class"""

    def __init__(self):
        """Initialize a new DB instance"""
        TRADEHUB_DB_USER = getenv("TRADEHUB_DB_USER")
        TRADEHUB_DB_PWD = getenv("TRADEHUB_DB_PWD")
        TRADEHUB_DB_HOST = getenv("TRADEHUB_DB_HOST")
        TRADEHUB_DB_PORT = getenv("TRADEHUB_DB_PORT")
        TRADEHUB_DB = getenv("TRADEHUB_DB")

        try:
            self._engine = create_engine("postgresql+psycopg2://{}:{}@{}:{}/{}"
                                         .format(TRADEHUB_DB_USER,
                                                 TRADEHUB_DB_PWD,
                                                 TRADEHUB_DB_HOST,
                                                 TRADEHUB_DB_PORT,
                                                 TRADEHUB_DB))
        except Exception as e:
            print("Error while connecting to the Database", e)

        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Represents a Memoized session object"""
        if self.__session is None:
            session_factory = sessionmaker(bind=self._engine)
            DBSession = scoped_session(session_factory)
            self.__session = DBSession()
        return self.__session

    def all(self, cls=None):
        """Retrieves all objects of a class"""
        new = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls == clss:
                objs = self._session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new[key] = obj
        return new

    def new(self, obj):
        """Adds the object to the current database session"""
        self._session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self._session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj is not None:
            self._session.delete(obj)

    def get(self, cls, id):
        """Retrieves an object from the database by id"""
        if cls is not None and id is not None:
            obj = self._session.get(cls, id)
            return obj
        return None

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds new user to database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self.save()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Finds user by key-word argument"""
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates user"""
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError("User not found")

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError(f"Attribute {key} not found on User")
        self.save()

    def close(self):
        """Closes the current DB session"""
        self._session.remove()
