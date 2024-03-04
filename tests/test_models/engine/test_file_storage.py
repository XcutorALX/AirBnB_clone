#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
"""Test case for FileStorage class"""

class TestFileStorage(unittest.TestCase):
    def tearDown(self):
        with open("file.json", encoding="utf-8") as f:
            pass

    def test_module_docstring(self):
        """Test for docstring in the base_model module"""

        docstr = __import__("models.engine.file_storage").__doc__
        self.assertEqual(True, len(docstr) > 0)

    def test_new(self):
        """Test the new method of storage class"""

        storage = FileStorage()
        b1 = BaseModel()
        result = {f"{b1.__class__.__name__}.{b1.id}": b1}
        storage.new(b1)
        test = FileStorage.__dict__["_FileStorage__objects"].copy()
        self.assertEqual(result, test)

        b2 = BaseModel()
        result[f"{b2.__class__.__name__}.{b2.id}"] = b2
        test = FileStorage.__dict__["_FileStorage__objects"].copy()
        self.assertEqual(result, test)
