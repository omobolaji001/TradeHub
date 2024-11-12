#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db
from models.user import User
from models.base import BaseModel
from models.business import Business
from models.product import Product
from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
from models.shipment import Shipment
from models.category import Category
import json
import os
import unittest

DBStorage = db.DB
classes = {"Shipment": Shipment, "Cart": Cart, "Product": Product,
           "Category": Category, "Payment": Payment, "User": User
           "Order": Order, "OrderItem": OrderItem, "CartItem": CartItem
           "Business": Business}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_db_storage_module_docstring(self):
        """Test for the db.py module docstring"""
        self.assertIsNot(db.__doc__, None,
                         "db.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBS class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DB class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DB class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DB methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBStorage(unittest.TestCase):
    """Test the DB class"""
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)
