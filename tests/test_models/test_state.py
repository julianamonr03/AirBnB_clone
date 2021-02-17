#!/usr/bin/python3
'''test state'''

import unittest
import models
import sys
from models.state import State


class test_State(unittest.TestCase):
    """ Test state"""

    def test_type_name(self):
        """test type"""
        self.assertIsInstance(State.name, str)

    def test_instance_in_object(self):
        """test instance in objects"""
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(State.name, "")

if __name__ == "__main__":
    unittest.main()
