#!/usr/bin/python3
# Unit Test for the Review class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestAmenity(unittest.TestCase):
    '''Tests the Review class
    '''

    def setUp(self):
        '''Instantiates a Place object
        '''
        self.review = Review()

    def test_instance_type(self):
        '''Tests the type of a Review instance
        '''
        self.assertIs(type(self.review), Review)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.review, BaseModel))

    # Test attributes

    def test_place_id_type(self):
        '''Tests the type of the place_id attribute
        '''
        self.assertIs(type(self.review.place_id), str)

    def test_place_id_value(self):
        '''Tests the value of the place_id attribute
        '''
        self.assertEqual(self.review.place_id, '')

    def test_user_id_type(self):
        '''Tests the type of the user_id attribute
        '''
        self.assertIs(type(self.review.user_id), str)

    def test_user_id_value(self):
        '''Tests the value of user_id
        '''
        self.assertEqual(self.review.user_id, '')

    def test_text_type(self):
        '''Tests the type of the text attribute
        '''
        self.assertIs(type(self.review.text), str)

    def test_text_value(self):
        '''Tests the value of text attribute
        '''
        self.assertEqual(self.review.text, '')

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.review.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.review.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.review.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.review.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.review.__class__, Review)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[Review] ({}) {}'.format(self.review.id, self.review.__dict__)
        self.assertEqual(self.review.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.review.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'Review'
        self.assertEqual(self.review.to_dict(), dictionary)
