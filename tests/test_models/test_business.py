#!/usr/bin/python3
"""Test Business for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
from models import business
from models.base import BaseModel
import time
import unittest
from unittest import mock
Business = business.Business
module_doc = models.base.__doc__


class TestBusinessDocs(unittest.TestCase):
    """Tests to check the documentation and style of Business class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.business_f = inspect.getmembers(Business, inspect.isfunction)

    def test_business_module_docstring(self):
        """Test for the business.py module docstring"""
        self.assertIsNot(business.__doc__, None,
                         "business.py needs a docstring")
        self.assertTrue(len(business.__doc__) >= 1,
                        "business.py needs a docstring")

    def test_business_class_docstring(self):
        """Test for the Business class docstring"""
        self.assertIsNot(Business.__doc__, None,
                         "Business class needs a docstring")
        self.assertTrue(len(Business.__doc__) >= 1,
                        "Business class needs a docstring")

    def test_business_func_docstrings(self):
        """Test for the presence of docstrings in Business methods"""
        for func in self.business_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBusiness(unittest.TestCase):
    """ Tests to check the Business class """

    def test_is_subclass(self):
        """ Tests that Business is a subclass of BaseModel """
        business = Business()
        self.assertIsInstance(business, BaseModel)
        self.assertTrue(hasattr(business, "id"))
        self.assertTrue(hasattr(business, "created_at"))
        self.assertTrue(hasattr(business, "updated_at"))

    def test_merchant_id_attr(self):
        """ Tests that Business has merchant_id attr """
        business = Business()
        self.assertTrue(hasattr(business, "merchant_id"))
        self.assertEqual(business.merchant_id, None)

    def test_name_attr(self):
        """ Tests that Business has name attr, and it's an empty string """
        business = Business()
        self.assertTrue(hasattr(business, "name"))
        self.assertEqual(business.name, None)

    def test_description_attr(self):
        """ Tests that Business has description attr, and it's an empty string """
        business = Business()
        self.assertTrue(hasattr(business, "description"))
        self.assertEqual(business.description, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        business = Business()
        new_d = business.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in business.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        b = Business()
        new_d = b.to_dict()
        self.assertEqual(new_d["__class__"], "Business")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], b.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], b.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        business = Business()
        string = "[Business] ({}) {}".format(business.id, business.__dict__)
        self.assertEqual(string, str(business))
