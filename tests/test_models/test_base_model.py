#!/usr/bin/python3
# Unit Tests for the BaseModel class

import unittest
from datetime import datetime
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

    # Test instance attributes

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.base.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.base.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.base.updated_at), datetime)

    def test_class_type(self):
        '''Tests the type of the __class__ attribute
        '''
        self.assertIs(type(self.base.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.base.__class__, BaseModel)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        form = '[BaseModel] ({}) {}'.format(self.base.id, self.base.__dict__)
        self.assertEqual(self.base.__str__(), form)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.base.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'BaseModel'
        self.assertEqual(self.base.to_dict(), dictionary)
