#!/usr/bin/python3
"""Test OrderItem for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import order_item
from models.base import BaseModel
import time
import unittest
from unittest import mock
module_doc = models.base.__doc__
OrderItem = order_item.OrderItem


class TestOrderItemDocs(unittest.TestCase):
    """Tests to check the documentation and style of OrderItem class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.order_item_f = inspect.getmembers(OrderItem, inspect.isfunction)

    def test_order_item_module_docstring(self):
        """Test for the order_item.py module docstring"""
        self.assertIsNot(order_item.__doc__, None,
                         "order_item.py needs a docstring")
        self.assertTrue(len(order_item.__doc__) >= 1,
                        "order_item.py needs a docstring")

    def test_order_item_class_docstring(self):
        """Test for the OrderItem class docstring"""
        self.assertIsNot(OrderItem.__doc__, None,
                         "OrderItem class needs a docstring")
        self.assertTrue(len(OrderItem.__doc__) >= 1,
                        "OrderItem class needs a docstring")

    def test_order_item_func_docstrings(self):
        """Test for the presence of docstrings in OrderItem methods"""
        for func in self.order_item_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOrderItem(unittest.TestCase):
    """ Tests to check the OrderItem class """

    def test_is_subclass(self):
        """ Tests that OrderItem is a subclass of BaseModel """
        item = OrderItem()
        self.assertIsInstance(item, BaseModel)
        self.assertTrue(hasattr(item, "id"))
        self.assertTrue(hasattr(item, "created_at"))
        self.assertTrue(hasattr(item, "updated_at"))

    def test_order_id_attr(self):
        """ Tests that OrderItem has order_id attr """
        item = OrderItem()
        self.assertTrue(hasattr(item, "order_id"))
        self.assertEqual(item.order_id, None)

    def test_product_id_attr(self):
        """ Tests that OrderItem has product_id attr  """
        item = OrderItem()
        self.assertTrue(hasattr(item, "product_id"))
        self.assertEqual(item.product_id, None)

    def test_quantity_attr(self):
        """ Tests that OrderItem has quantity attr """
        item = OrderItem()
        self.assertTrue(hasattr(item, "quantity"))
        self.assertEqual(item.quantity, None)

    def test_price_attr(self):
        """ Tests that OrderItem has price attr """
        item = OrderItem()
        self.assertTrue(hasattr(item, "price"))
        self.assertEqual(item.price, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        item = OrderItem()
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
        i = OrderItem()
        new_d = i.to_dict()
        self.assertEqual(new_d["__class__"], "OrderItem")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], i.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], i.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        item = OrderItem()
        string = "[OrderItem] ({}) {}".format(item.id, item.__dict__)
        self.assertEqual(string, str(item))
