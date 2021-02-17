#!/usr/bin/python3

"""
Unittest for FileStorage
"""

import uuid
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User



class Test_attributes(unittest.TestCase):
    """ Tests attributes """

    def test_new_data(self):
        """ test new entry """
        storage = FileStorage()
        data = storage.all()
        user = User()
        user.id = str(uuid.uuid4())
        user.name = "Juliana"
        storage.new(user)
        key = user.__class__.__name__ + "." + user.id
        self.assertIsNotNone(data[key])
    
    #def test_created_at(self):
        #""" test created_at """
        #self.assertEqual(type(BaseModel.created_at), datetime.datetime)
        #self.assertEqual(type(BaseModel.created_at), str)

    #def test_updated_at(self):
    #    """ test updated_at """
    #    self.assertEqual(type(self.updated_at), datetime.datetime)
    #    self.assertEqual(type(BaseModel.updated_at), str)

if __name__ == '__main__':
    unittest.main()
