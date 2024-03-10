from models.review import Review
from datetime import datetime
import unittest
"""This model contains the unnitest cases for the base model class"""


class TestReview(unittest.TestCase):
    """Test case for the Review class"""
    def tearDown(self):
        with open("file.json", encoding="utf-8", mode="w") as f:
            pass

    def test_module_docstring(self):
        """Tests for module docstring"""

        docstr = __import__("models.base_model").__doc__
        self.assertEqual(True, len(docstr) > 1)

    def test_instantization(self):
        """Instanties a Review class"""

        b1 = Review()
        self.assertEqual(Review, type(b1))

    def test_instantization_with_kwargs(self):
        """Tests the instantization of base model class with ***kwargs"""
        b1 = Review()
        inst = b1.__dict__.copy()
        inst["id"] = "7"
        inst2 = b1.to_dict()
        inst2["id"] = "7"
        model = {"__class__": "Review", "id": "7",
                 "updated_at": b1.updated_at.isoformat(),
                 "created_at": b1.created_at.isoformat()}
        b2 = Review(**model)
        self.assertEqual(inst, b2.__dict__)
        self.assertEqual(inst2, b2.to_dict())

    def test_created_at(self):
        """Tests the created_at attribute for a base model class"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        """Tests the updated_at attribute for a base model class"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_str(self):
        """Tests the string representation of a Review instance"""
        b1 = Review()
        val = f"[Review] ({b1.id}) {b1.__dict__}"
        self.assertEqual(val, str(b1))

    def test_save(self):
        """Tests the save method of the Review class"""
        b1 = Review()
        prev = b1.updated_at
        b1.save()
        self.assertEqual(True, b1.updated_at > prev)
