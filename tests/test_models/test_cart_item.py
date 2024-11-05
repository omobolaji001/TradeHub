#!/usr/bin/python3
"""Test CartItem for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import cart_item
from models.base import BaseModel
import time
import unittest
from unittest import mock
module_doc = models.base.__doc__
CartItem = cart_item.CartItem


class TestCartItemDocs(unittest.TestCase):
    """Tests to check the documentation and style of CartItem class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.cart_item_f = inspect.getmembers(CartItem, inspect.isfunction)

    def test_cart_item_module_docstring(self):
        """Test for the cart_item.py module docstring"""
        self.assertIsNot(cart_item.__doc__, None,
                         "cart_item.py needs a docstring")
        self.assertTrue(len(cart_item.__doc__) >= 1,
                        "cart_item.py needs a docstring")

    def test_cart_item_class_docstring(self):
        """Test for the CartItem class docstring"""
        self.assertIsNot(CartItem.__doc__, None,
                         "CartItem class needs a docstring")
        self.assertTrue(len(CartItem.__doc__) >= 1,
                        "CartItem class needs a docstring")

    def test_cart_item_func_docstrings(self):
        """Test for the presence of docstrings in CartItem methods"""
        for func in self.cart_item_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCartItem(unittest.TestCase):
    """ Tests to check the CartItem class """

    def test_is_subclass(self):
        """ Tests that CartItem is a subclass of BaseModel """
        item = CartItem()
        self.assertIsInstance(item, BaseModel)
        self.assertTrue(hasattr(item, "id"))
        self.assertTrue(hasattr(item, "created_at"))
        self.assertTrue(hasattr(item, "updated_at"))

    def test_cart_id_attr(self):
        """ Tests that CartItem has cart_id attr """
        item = CartItem()
        self.assertTrue(hasattr(item, "cart_id"))
        self.assertEqual(item.cart_id, None)

    def test_product_id_attr(self):
        """ Tests that CartItem has product_id attr  """
        item = CartItem()
        self.assertTrue(hasattr(item, "product_id"))
        self.assertEqual(item.product_id, None)

    def test_quantity_attr(self):
        """ Tests that OrderItem has quantity attr """
        item = CartItem()
        self.assertTrue(hasattr(item, "quantity"))
        self.assertEqual(item.quantity, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        item = CartItem()
        new_d = item.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in item.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        i = CartItem()
        new_d = i.to_dict()
        self.assertEqual(new_d["__class__"], "CartItem")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], i.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], i.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        item = CartItem()
        string = "[CartItem] ({}) {}".format(item.id, item.__dict__)
        self.assertEqual(string, str(item))
