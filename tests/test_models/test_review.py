#!/usr/bin/python3
'''test review'''
import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """ Test review """

    def test_type_text(self):
        """ Verify if is instance"""
        self.assertIsInstance(Review.text, str)

    def test_instance_in_object(self):
        """test instance in objects"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

if __name__ == "__main__":
    unittest.main()
