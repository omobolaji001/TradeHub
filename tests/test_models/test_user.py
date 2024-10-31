#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
import time
import unittest
from unittest import mock
from models.order import Order
from models.shipment import Shipment
BaseModel = models.base.BaseModel
User = models.user.User
module_doc = models.base.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )

class TestUser(unittest.TestCase):
    """ Tests to check the User class """

    def test_is_subclass(self):
        """ Tests that User is a subclass of BaseModel """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_firstname_attr(self):
        """ Tests that User has firstname attr, and that it's empty string """
        user = User()
        self.assertTrue(hasattr(user, "firstname"))
        self.assertEqual(user.firstname, None)

    def test_lastname_attr(self):
        """ Tests that User has lastname attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "lastname"))
        self.assertEqual(user.lastname, None)

    def test_username_attr(self):
        """ Tests that User has username attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "username"))
        self.assertEqual(user.username, None)

    def test_email_attr(self):
        """ Tests that User has email attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, None)

    def test_password_attr(self):
        """ Tests that User has password attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, None)

    def test_phone_number_attr(self):
        """ Test that User has phone_number attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "phone_number"))
        self.assertEqual(user.phone_number, None)

    def test_reset_token_attr(self):
        """ Tests that User has reset_token attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "reset_token"))
        self.assertEqual(user.reset_token, None)

    def test_address_attr(self):
        """ Tests that User has address attr, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "address"))
        self.assertEqual(user.address, None)

    def test_role_attr(self):
        """ Tests that User has role attr """
        user = User()
        self.assertTrue(hasattr(user, "role"))
        self.assertEqual(user.role, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        user = User()
        new_d = user.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in user.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
