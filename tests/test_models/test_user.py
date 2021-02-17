#!/usr/bin/python3
"""
Unittest for User
"""


import unittest
from models.base_model import BaseModel
from models.user import User


class test_User(unittest.TestCase):
    """ Tests for attributes """

    def test_name(self):
        """ test id """
        self.assertIsInstance(User.first_name, str)

    def test_user(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

if __name__ == '__main__':
    unittest.main()
