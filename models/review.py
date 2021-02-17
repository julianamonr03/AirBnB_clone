#!/usr/bin/python3
""" State class that inhertis from BaseModel """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes from Review """

    place_id = ""
    user_id = ""
    text = ""
