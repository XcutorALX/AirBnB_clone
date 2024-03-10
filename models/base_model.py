#!/usr/bin/python3
"""This module coontains a BaseModel class"""


from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Instantization for an instance of a BaseModel class"""
        form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(val, form)
                elif key != "__class__":
                    self.__dict__[key] = val

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """String representation of a base model instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Save method for the BaseModel classs"""
        models.storage.save()
        self.updated_at = datetime.today()

    def to_dict(self):
        """Converts the instance into a dictionary format"""
        inst = self.__dict__.copy()
        inst["__class__"] = self.__class__.__name__
        inst["created_at"] = self.created_at.isoformat()
        inst["updated_at"] = self.updated_at.isoformat()
        return (inst)
