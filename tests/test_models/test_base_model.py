#!/usr/bin/python3
'''test models'''
import unittest
import re
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    '''test BaseModel'''

    def test_createAttr_noArgs(self):
        '''create Instance w/o args'''
        my_model = BaseModel()
        my_model.name = "Holberton"
        self.assertEqual(my_model.name, "Holberton")

    def test_id_noArgs(self):
        '''check type/value of id w/o args'''
        my_model = BaseModel()
        self.assertTrue(my_model.id)
        self.assertEqual(type(my_model.id), str)

    def test_created_at_noArgs_type(self):
        '''check type of created_at w/o args'''
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_created_at_noArgs_format(self):
        '''check format %Y-%M-%DT%H:%M:%S.%MS'''
        datetime_format = re.compile(
            "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+$")
        my_model = BaseModel()
        my_created_at = my_model.to_dict()['created_at']
        format_found = datetime_format.match(my_created_at)
        self.assertIsNotNone(format_found)

    def test_created_at_noArgs_value(self):
        '''check value of created_at w/o args'''
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        self.assertEqual(my_model.created_at.replace(microsecond=0), now)

    def test_created_at_noArgs_afterSave(self):
        '''check created_at w/o args after save()'''
        my_model = BaseModel()
        my_created_at = my_model.created_at
        my_model.save()
        self.assertEqual(my_model.created_at, my_created_at)

    def test_updated_at_noArgs_type(self):
        '''check type updated_at'''
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_updated_at_noArgs_format(self):
        '''check format %Y-%M-%DT%H:%M:%S.%MS'''
        datetime_format = re.compile(
            "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+$")
        my_model = BaseModel()
        my_updated_at = my_model.to_dict()['updated_at']
        format_found = datetime_format.match(my_updated_at)
        self.assertIsNotNone(format_found)

    def test_updated_at_noArgs_value(self):
        '''check value of updated_at'''
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        self.assertEqual(my_model.updated_at.replace(microsecond=0), now)

    def test_updated_at_noArgs_value_afterSave(self):
        '''check value of updated_at after save()'''
        my_model = BaseModel()
        updated_pre = my_model.updated_at
        my_model.save()
        self.assertTrue(my_model.updated_at > updated_pre)

    def test_str(self):
        '''check __str__ method'''
        my_model = BaseModel()
        r = re.compile("\[BaseModel\] (.*) {.*}")
        my_str = my_model.__str__()
        self.assertIsNotNone(r.match(my_str))

    def test_to_dict_noAditonalAttr(self):
        '''check to_dict w/o additional Attributes'''
        my_model = BaseModel()
        BaseModel.name = "holberton"
        attributes = {}
        for key, value in my_model.to_dict().items():
            if (key not in ('__class__', 'id', 'created_at', 'updated_at')):
                attributes[key] = value
        self.assertFalse(attributes)
