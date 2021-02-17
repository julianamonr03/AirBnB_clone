#!/usr/bin/python3
""" Base Model file """


import uuid
from datetime import datetime
import models


format_iso = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        '''Initialize public instance attributes'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, format_iso)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        ''' Should print: [<class name>] (<self.id>) <self.__dict__> '''
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    """
    Public Instances Methods
    """

    def save(self):
        ''' Updates the public instance attribute updated_at
        with the current datetime '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance '''
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return (dic)
