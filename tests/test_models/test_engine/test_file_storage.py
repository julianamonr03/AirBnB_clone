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

if __name__ == '__main__':
    unittest.main()
