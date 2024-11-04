#!/usr/bin/python3
"""Test Cart for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import cart
from models.base import BaseModel
import time
import unittest
from unittest import mock
module_doc = models.base.__doc__
Cart = cart.Cart


class TestCartDocs(unittest.TestCase):
    """Tests to check the documentation and style of Cart class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.cart_f = inspect.getmembers(Cart, inspect.isfunction)

    def test_cart_module_docstring(self):
        """Test for the cart.py module docstring"""
        self.assertIsNot(cart.__doc__, None,
                         "cart.py needs a docstring")
        self.assertTrue(len(cart.__doc__) >= 1,
                        "cart.py needs a docstring")

    def test_cart_class_docstring(self):
        """Test for the Cart class docstring"""
        self.assertIsNot(Cart.__doc__, None,
                         "Cart class needs a docstring")
        self.assertTrue(len(Cart.__doc__) >= 1,
                        "Cart class needs a docstring")

    def test_cart_func_docstrings(self):
        """Test for the presence of docstrings in Cart methods"""
        for func in self.cart_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCart(unittest.TestCase):
    """ Tests to check the Cart class """

    def test_is_subclass(self):
        """ Tests that Cart is a subclass of BaseModel """
        cart = Cart()
        self.assertIsInstance(cart, BaseModel)
        self.assertTrue(hasattr(cart, "id"))
        self.assertTrue(hasattr(cart, "created_at"))
        self.assertTrue(hasattr(cart, "updated_at"))

    def test_customer_id_attr(self):
        """ Tests that Order has customer_id attr """
        cart = Cart()
        self.assertTrue(hasattr(cart, "customer_id"))
        self.assertEqual(cart.customer_id, None)

    def test_total_amount_attr(self):
        """ Tests that Cart has total_amount attr """
        cart = Cart()
        self.assertTrue(hasattr(cart, "total_amount"))
        self.assertEqual(cart.total_amount, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        cart = Cart()
        new_d = cart.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in cart.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Cart()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Cart")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        cart = Cart()
        string = "[Cart] ({}) {}".format(cart.id, cart.__dict__)
        self.assertEqual(string, str(cart))
