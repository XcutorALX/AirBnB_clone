"""Contains test modules for the console.py module"""

import unittest
import models
import os
import sys
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from uuid import uuid4


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = models.engine.file_storage.FileStorage()
        cls.classes = ["User", "BaseModel", "Place", "Amenity", "City"]

    def setUp(self):
        self.storage = TestConsole.storage
        self.storage.reload()

    def tearDown(self):
        with open("file.json", mode='w') as f:
            pass

    def test_empty_line(self):
        """Tests the console's behavior to an empty line"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")

        out = f.getvalue().rstrip("\n")
        self.assertEqual(out, "")

    def test_precmd(self):
        """Tests the precmd method called on commands
        before being interpreted"""

        result = HBNBCommand().precmd("User.create()")
        self.assertEqual(result, "create User")
        result = HBNBCommand().precmd("BaseModel.create(name, age)")
        self.assertEqual(result, "create BaseModel name age")
        result = HBNBCommand().precmd("User.update(023#LWJ45R532,\
                 name, Unchained)")
        self.assertEqual(result, "update User 023#LWJ45R532 name Unchained")
        dictStr = "{ 'name': 'Lekan', 'age': 300, 'height': '6'7' }"
        result = HBNBCommand().precmd("Place.update(023#LWJ45R543, "
                                      + dictStr + ')')
        self.assertEqual(result, f"update Place 023#LWJ45R543 {dictStr}")
        result = HBNBCommand().precmd("Place.update(023#LWJ45R543 "
                                      + dictStr + ')')
        self.assertEqual(result, f"update Place 023#LWJ45R543 {dictStr}")

    def test_quit(self):
        """Tests the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("quit")
            self.assertEqual(result, True)

        out = f.getvalue().rstrip("\n")
        self.assertEqual(out, "")

    def test_EOF(self):
        """Tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd("EOF")
            self.assertEqual(result, True)
        out = f.getvalue().rstrip("\n")
        self.assertEqual(out, "")


class TestCreate(unittest.TestCase):
    """Test case for the create command"""

    @classmethod
    def setUpClass(cls):
        cls.storage = models.engine.file_storage.FileStorage()
        cls.classes = ["User", "BaseModel", "Place", "Amenity", "City"]

    def setUp(self):
        self.storage = TestConsole.storage
        self.storage.reload()

    def tearDown(self):
        with open("file.json", mode='w') as f:
            pass

    def test_create_no_error(self):
        """Tests creation of instances with the format
        '<class name>.create()'"""
        for cls in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{cls}.create()")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            result = f"{cls}.{out}" in self.storage.all()
            self.assertEqual(True, result)

    def test_do_create_no_error(self):
        """Tests creation of instances with the format 'create <class name>'"""
        for cls in TestConsole.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {cls}")
            out = f.getvalue().rstrip("\n")
            result = f"{cls}.{out}" in self.storage.all()
            self.assertEqual(True, result)

    def test_create_error_class_missing(self):
        """Tests the errors of the create function with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        out = f.getvalue().rstrip("\n")
        self.assertEqual(out, "** class name missing **")

    def test_create_error_invalid_class(self):
        """Tests the error output for invalid class"""
        invalid_classes = ["Man", "Tree", "Bag", "Boy", "Woman", "girl"]
        for cls in invalid_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {cls}")
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** class doesn't exist **")

            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{cls}.create()")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** class doesn't exist **")


class TestShow(unittest.TestCase):
    """Tests the show command"""

    @classmethod
    def setUpClass(cls):
        cls.storage = models.engine.file_storage.FileStorage()
        cls.classes = ["User", "BaseModel", "Place", "Amenity", "City"]

    def setUp(self):
        self.storage = TestConsole.storage
        self.storage.reload()

    def tearDown(self):
        with open("file.json", mode='w') as f:
            pass

    def test_show(self):
        """Tests the show command with good input"""
        original_stdout = sys.stdout
        with open(os.devnull, 'w') as f:
            sys.stdout = f
            for i in range(10):
                for cls in TestConsole.classes:
                    HBNBCommand().onecmd(f"create {cls}")
            sys.stdout = original_stdout

        classes = self.storage.all()
        for cls in classes:
            args = cls.split(".")
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {args[0]} {args[1]}")
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, str(classes[cls]))

            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{args[0]}.show({args[1]})")
                self.assertEqual(command, f"show {args[0]} {args[1]}")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, str(classes[cls]))

    def test_show_missing_class(self):
        """Tests the show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show")
        out = f.getvalue().rstrip("\n")
        self.assertEqual(out, "** class name missing **")

    def test_show_invalid_class(self):
        """Tests the show command with invalid classes"""

        invalid_classes = ["Man", "Tree", "Bag", "Boy", "Woman", "girl"]
        for cls in invalid_classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {cls}")
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** class doesn't exist **")

            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{cls}.show()")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** class doesn't exist **")

    def test_show_missing_id(self):
        """Tests the show command with missing id"""

        for cls in TestShow.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {cls}")
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** instance id missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{cls}.show()")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** instance id missing **")

    def test_show_invalid_id(self):
        """Tests the show command with invalid id"""

        for cls in TestShow.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show {cls} {uuid4()}")
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** no instance found **")

            with patch('sys.stdout', new=StringIO()) as f:
                command = HBNBCommand().precmd(f"{cls}.show({uuid4()})")
                HBNBCommand().onecmd(command)
            out = f.getvalue().rstrip("\n")
            self.assertEqual(out, "** no instance found **")


class TestDestroy(unittest.TestCase):
    """Test case for the destroy command"""

    @classmethod
    def setUpClass(cls):
        cls.storage = models.engine.file_storage.FileStorage()
        cls.classes = ["User", "BaseModel", "Place", "Amenity", "City"]

    def setUp(self):
        self.storage = TestConsole.storage
        self.storage.reload()

    def tearDown(self):
        with open("file.json", mode='w') as f:
            pass

    def test_destroy_no_errors(self):
        """Tests the destroy function"""
        original_stdout = sys.stdout
        with open(os.devnull, 'w') as f:
            sys.stdout = f
            for i in range(10):
                for cls in TestConsole.classes:
                    HBNBCommand().onecmd(f"create {cls}")
            sys.stdout = original_stdout

        clsObjs = self.storage.all()
        clsKeys = [i for i in clsObjs]
        i = 0
        for cls in clsKeys:
            args = cls.split(".")
            if (i < len(TestDestroy.classes) * 5):
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"destroy {args[0]} {args[1]}")
                    result = cls not in self.storage.all()
                    self.assertEqual(result, True)
                out = f.getvalue().rstrip("\n")
                self.assertEqual(out, "")
            else:
                with patch('sys.stdout', new=StringIO()) as f:
                    command = HBNBCommand().precmd(f"{args[0]}.\
                                                    destroy({args[1]})")
                    HBNBCommand().onecmd(command)
                    result = cls not in self.storage.all()
                    self.assertEqual(result, True)
                out = f.getvalue().rstrip("\n")
                self.assertEqual(out, "")
            i += 1
