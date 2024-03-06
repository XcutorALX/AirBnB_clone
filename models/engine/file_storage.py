#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""This module contains a FileStorage class"""


class FileStorage:
    """A class that serializes instances to a
    JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): The name of the file to save objects to
        __objects (dict): A dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class>.id

        Args:
            obj (dict): the object to be added ti ___objects
        """

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def all(self):
        """Returns all objects stored in __objects"""
        return (FileStorage.__objects)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        if FileStorage.__objects == {}:
            return

        objDict = {i: FileStorage.__objects[i].to_dict()
                   for i in FileStorage.__objects}
        with open(FileStorage.__file_path, mode="w", encoding='utf-8') as f:
            json.dump(objDict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        class_mapping = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as f:
                value = json.load(f)
                objs = {i: class_mapping[value[i]["__class__"]](**value[i])
                        for i in value}
                FileStorage.__objects = objs
        except (json.JSONDecodeError, FileNotFoundError) as e:
            if isinstance(e, json.JSONDecodeError):
                FileStorage.__objects = {}
            pass
