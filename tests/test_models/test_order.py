#!/usr/bin/python3
"""Test Order for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import order
from models.base import BaseModel
import time
import unittest
from unittest import mock
module_doc = models.base.__doc__
Order = order.Order


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of Order class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.order_f = inspect.getmembers(Order, inspect.isfunction)

    def test_order_module_docstring(self):
        """Test for the order.py module docstring"""
        self.assertIsNot(order.__doc__, None,
                         "order.py needs a docstring")
        self.assertTrue(len(order.__doc__) >= 1,
                        "order.py needs a docstring")

    def test_order_class_docstring(self):
        """Test for the Order class docstring"""
        self.assertIsNot(Order.__doc__, None,
                         "Order class needs a docstring")
        self.assertTrue(len(Order.__doc__) >= 1,
                        "Order class needs a docstring")

    def test_order_func_docstrings(self):
        """Test for the presence of docstrings in Order methods"""
        for func in self.order_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOrder(unittest.TestCase):
    """ Tests to check the Order class """

    def test_is_subclass(self):
        """ Tests that Order is a subclass of BaseModel """
        order = Order()
        self.assertIsInstance(order, BaseModel)
        self.assertTrue(hasattr(order, "id"))
        self.assertTrue(hasattr(order, "created_at"))
        self.assertTrue(hasattr(order, "updated_at"))

    def test_customer_id_attr(self):
        """ Tests that Order has customer_id attr """
        order = Order()
        self.assertTrue(hasattr(order, "customer_id"))
        self.assertEqual(order.customer_id, None)

    def test_order_date_attr(self):
        """ Tests that Order has order_date attr  """
        order = Order()
        self.assertTrue(hasattr(order, "order_date"))
        self.assertEqual(order.order_date, None)

    def test_status_attr(self):
        """ Tests that Order has status attr """
        order = Order()
        self.assertTrue(hasattr(order, "status"))
        self.assertEqual(order.status, None)

    def test_total_amount_attr(self):
        """ Tests that Order has total_amount attr """
        order = Order()
        self.assertTrue(hasattr(order, "total_amount"))
        self.assertEqual(order.total_amount, None)


    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        order = Order()
        new_d = order.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in order.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        o = Order()
        new_d = o.to_dict()
        self.assertEqual(new_d["__class__"], "Order")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], o.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], o.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        order = Order()
        string = "[Order] ({}) {}".format(order.id, order.__dict__)
        self.assertEqual(string, str(order))
