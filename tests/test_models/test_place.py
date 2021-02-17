#!/usr/bin/python3
'''test place'''

import unittest
from models.base_model import BaseModel
from models.place import Place


class test_Place(unittest.TestCase):
    """ Test place """

    def test_type_bathrooms(self):
        """ Verify if is instance"""
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_type_rooms(self):
        self.assertIsInstance(Place.number_rooms, int)
    
    def test_type_latitude(self):
        self.assertIsInstance(Place.latitude, float)

    def test_type_longitude(self):
        self.assertIsInstance(Place.longitude, float)

    def test_instance_in_object(self):
        """test instance in objects"""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

if __name__ == "__main__":
    unittest.main()
