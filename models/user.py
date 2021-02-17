#!/usr/bin/python3
""" New class User that inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """ New Class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
