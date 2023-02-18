#!/usr/bin/python3
# unit testing for console


import unittest
import sys
from datetime import datetime
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


class TestAllConsole(unittest.TestCase):
    """test base clas"""
    def test_create(self):
        """test create with no class"""
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(message, f.getvalue().strip())

    def test_create_wrongclass(self):
        """create with wrong class"""
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_noclass(self):
        """testimg show with no class"""
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_noid(self):
        """test show without an id"""
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_classname(self):
        """test show with none existing class name"""
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_wrongid(self):
        """show with wrong id"""
        message = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 124456"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_noclass(self):
        """test all with no class"""
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(message, f.getvalue().strip())

    def test_all_wrongclass(self):
        """test sll with wrong class"""
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_noid(self):
        """test all eith no id"""
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_wrongid(self):
        """test update with wrong id"""
        message = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User 124456"))
            self.assertEqual(message, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
