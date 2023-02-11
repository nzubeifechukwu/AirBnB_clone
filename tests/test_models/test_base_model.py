#!/usr/bin/python3
# Unit Tests for the BaseModel class

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Tests the BaseModel class
    '''

    def setUp(self):
        '''Initializes a BaseModel instance
        '''
        self.base = BaseModel()

    def test_instance_type(self):
        '''Tests if instance type is BaseModel
        '''
        self.assertIs(type(self.base), BaseModel)

    def test_attribute_types
