#!/usr/bin/python3
"""Test Product for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import product
from models.base import BaseModel
import time
import unittest
from unittest import mock
Product = product.Product
module_doc = models.base.__doc__


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of Product class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.product_f = inspect.getmembers(Product, inspect.isfunction)

    def test_product_module_docstring(self):
        """Test for the product.py module docstring"""
        self.assertIsNot(product.__doc__, None,
                         "product.py needs a docstring")
        self.assertTrue(len(product.__doc__) >= 1,
                        "product.py needs a docstring")

    def test_product_class_docstring(self):
        """Test for the Product class docstring"""
        self.assertIsNot(Product.__doc__, None,
                         "Product class needs a docstring")
        self.assertTrue(len(Product.__doc__) >= 1,
                        "Product class needs a docstring")

    def test_product_func_docstrings(self):
        """Test for the presence of docstrings in Product methods"""
        for func in self.product_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestProduct(unittest.TestCase):
    """ Tests to check the Product class """

    def test_is_subclass(self):
        """ Tests that Product is a subclass of BaseModel """
        product = Product()
        self.assertIsInstance(product, BaseModel)
        self.assertTrue(hasattr(product, "id"))
        self.assertTrue(hasattr(product, "created_at"))
        self.assertTrue(hasattr(product, "updated_at"))

    def test_business_id_attr(self):
        """ Tests that Product has business_id attr """
        product = Product()
        self.assertTrue(hasattr(product, "business_id"))
        self.assertEqual(product.business_id, None)

    def test_category_id_attr(self):
        """ Tests that Product has category_id attr  """
        product = Product()
        self.assertTrue(hasattr(product, "category_id"))
        self.assertEqual(product.category_id, None)

    def test_name_attr(self):
        """ Tests that Product has name attr, and it's an empty string """
        product = Product()
        self.assertTrue(hasattr(product, "name"))
        self.assertEqual(product.name, None)

    def test_description_attr(self):
        """ Tests that Product has description attr, and it's an empty string """
        product = Product()
        self.assertTrue(hasattr(product, "description"))
        self.assertEqual(product.description, None)

    def test_price_attr(self):
        """ Tests that Product has price attr """
        product = Product()
        self.assertTrue(hasattr(product, "price"))
        self.assertEqual(product.price, None)

    def test_stock_attr(self):
        """ Test that Product has stock attr """
        product = Product()
        self.assertTrue(hasattr(product, "stock"))
        self.assertEqual(product.stock, None)


    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        product = Product()
        new_d = product.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in product.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Product()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Product")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        product = Product()
        string = "[Product] ({}) {}".format(product.id, product.__dict__)
        self.assertEqual(string, str(product))
