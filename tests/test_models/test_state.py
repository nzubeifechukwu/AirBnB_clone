#!/usr/bin/python3
# Unit Test for the State class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestAmenity(unittest.TestCase):
    '''Tests the State class
    '''

    def setUp(self):
        '''Instantiates a State object
        '''
        self.state = State()

    def test_instance_type(self):
        '''Tests the type of a State instance
        '''
        self.assertIs(type(self.state), State)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.state, BaseModel))

    # Test attributes

    def test_name_type(self):
        '''Tests the type of the name attribute
        '''
        self.assertIs(type(self.state.name), str)

    def test_name_value(self):
        '''Tests the value of name attribute
        '''
        self.assertEqual(self.state.name, '')

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.state.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.state.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.state.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.state.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.state.__class__, State)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[State] ({}) {}'.format(self.state.id, self.state.__dict__)
        self.assertEqual(self.state.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.state.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'State'
        self.assertEqual(self.state.to_dict(), dictionary)
