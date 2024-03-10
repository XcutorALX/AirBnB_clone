#!/usr/bin/python3
"""This module contains a Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class representation of a review"""

    place_id = ""
    user_id = ""
    text = ""
