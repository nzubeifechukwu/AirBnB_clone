#!/usr/bin/python3
# Unit Test for the City class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestAmenity(unittest.TestCase):
    '''Tests the City class
    '''

    def setUp(self):
        '''Instantiates a City object
        '''
        self.city = City()

    def test_instance_type(self):
        '''Tests the type of an Amenity instance
        '''
        self.assertIs(type(self.city), City)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.city, BaseModel))

    # Test attributes

    def test_state_id_type(self):
        '''Tests the type of the state_id attribute
        '''
        self.assertIs(type(self.city.state_id), str)

    def test_state_id_value(self):
        '''Tests the value of the state_id attribute
        '''
        self.assertEqual(self.city.state_id, '')

    def test_name_type(self):
        '''Tests the type of the name attribute
        '''
        self.assertIs(type(self.city.name), str)

    def test_name_value(self):
        '''Tests the value of name attribute
        '''
        self.assertEqual(self.city.name, '')

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.city.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.city.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.city.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.city.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.city.__class__, City)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[City] ({}) {}'.format(self.city.id, self.city.__dict__)
        self.assertEqual(self.city.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.city.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'City'
        self.assertEqual(self.city.to_dict(), dictionary)
