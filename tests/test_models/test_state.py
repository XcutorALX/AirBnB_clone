from models.state import State
from datetime import datetime
import unittest
"""This model contains the unnitest cases for the base model class"""


class TestState(unittest.TestCase):
    """Test case for the State class"""
    def tearDown(self):
        with open("file.json", encoding="utf-8", mode="w") as f:
            pass

    def test_module_docstring(self):
        """Tests for module docstring"""

        docstr = __import__("models.base_model").__doc__
        self.assertEqual(True, len(docstr) > 1)

    def test_instantization(self):
        """Instanties a State class"""

        b1 = State()
        self.assertEqual(State, type(b1))

    def test_instantization_with_kwargs(self):
        """Tests the instantization of base model class with ***kwargs"""
        b1 = State()
        inst = b1.__dict__.copy()
        inst["id"] = "7"
        inst2 = b1.to_dict()
        inst2["id"] = "7"
        model = {"__class__": "State", "id": "7",
                 "updated_at": b1.updated_at.isoformat(),
                 "created_at": b1.created_at.isoformat()}
        b2 = State(**model)
        self.assertEqual(inst, b2.__dict__)
        self.assertEqual(inst2, b2.to_dict())

    def test_created_at(self):
        """Tests the created_at attribute for a base model class"""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        """Tests the updated_at attribute for a base model class"""
        self.assertEqual(datetime, type(State().updated_at))

    def test_str(self):
        """Tests the string representation of a State instance"""
        b1 = State()
        val = f"[State] ({b1.id}) {b1.__dict__}"
        self.assertEqual(val, str(b1))

    def test_save(self):
        """Tests the save method of the State class"""
        b1 = State()
        prev = b1.updated_at
        b1.save()
        self.assertEqual(True, b1.updated_at > prev)
