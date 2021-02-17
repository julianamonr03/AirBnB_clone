#!/usr/bin/python3
'''test amenity '''

import unittest
import sys
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ Test amenity """

    def test_name(self):
        self.assertEqual(type(Amenity.name), str)

    def test_instance_in_object(self):
        """ Test instances """
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertEqual(Amenity.name, "")

if __name__ == "__main__":
    unittest.main()
