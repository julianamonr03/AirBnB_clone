#!/usr/bin/python3
'''test state'''

import unittest
import models
import sys
from models.city import City
from models.base_model import BaseModel

class test_City(unittest.TestCase):
    """ Test city """

    def test_instance_in_object(self):
        """test instance in objects"""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def is_instace(self):
        self.assertIsInstance(City, BaseModel)

if __name__ == "__main__":
    unittest.main()
