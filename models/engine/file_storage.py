#!/usr/bin/python3
""" Class FileStorage """

import json
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage():
    ''' Private class attributes '''

    __file_path = "file.json"
    __objects = {}

    """ Public instance methods """

    def all(self):
        ''' Returns the dictionary __objects '''
        return (self.__objects)

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id '''
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        ''' SERIALIZES __objects to the JSON file (path: __file_path) '''
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        ''' DESERIALIZES the JSON file to __objects
        (only if the JSON file (__file_path) exists '''
        try:
            with open(self.__file_path, 'r') as f:
                file_json = json.load(f)
            for key, value in file_json.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
