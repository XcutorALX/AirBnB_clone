#!/usr/bin/python3
from models.base_model import BaseModel
"""This module contains a Review class"""


class Review(BaseModel):
    """Class representation of a review"""

    place_id = ""
    user_id = ""
    text = ""
