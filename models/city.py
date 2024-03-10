#!/usr/bin/python3
"""This module contains a City class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class representation of a city"""

    state_id = ""
    name = ""
