#!/usr/bin/python3
# Tests the Amenity class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''Tests the Amenity class
    '''

    def setUp(self):
        '''Instantiates an Amenity object
        '''
        self.amenity = Amenity()

    def test_instance_type(self):
        '''Tests the type of an Amenity instance
        '''
        self.assertIs(type(self.amenity), Amenity)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.amenity, BaseModel))

    # Test attributes

    def test_name_type(self):
        '''Tests the type of the name attribute
        '''
        self.assertIs(type(self.amenity.name), str)

    def test_name_value(self):
        '''Tests the value of name attribute
        '''
        self.assertEqual(self.amenity.name, '')

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.amenity.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.amenity.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.amenity.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.amenity.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.amenity.__class__, Amenity)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[Amenity] ({}) {}'.format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(self.amenity.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.amenity.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'Amenity'
        self.assertEqual(self.amenity.to_dict(), dictionary)
