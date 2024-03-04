#!/usr/bin/python3
from datetime import datetime
import models
from uuid import uuid4
"""This module contains a base class"""


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
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
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        models.storage.save()
        self.updated_at = datetime.today()

    def to_dict(self):
        inst = self.__dict__.copy()
        inst["__class__"] = self.__class__.__name__
        inst["created_at"] = self.created_at.isoformat()
        inst["updated_at"] = self.updated_at.isoformat()
        return (inst)
