#!/usr/bin/python3
# Tests for the FileStorage class

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''Tests the FileStorage class
    '''

    def setUp(self):
        '''Instantiates a FileStorage object
        '''
        self.storage = FileStorage()

    def test_instance_type(self):
        '''Tests the instance type
        '''
        self.assertIs(type(self.storage), FileStorage)

    def test_all_type(self):
        '''Tests the type of the all method
        '''
        self.assertIs(type(self.storage.all()), dict)
