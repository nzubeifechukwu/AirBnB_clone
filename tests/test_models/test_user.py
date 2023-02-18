#!/usr/bin/python3
# Unit Test for the User class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestAmenity(unittest.TestCase):
    '''Tests the User class
    '''

    def setUp(self):
        '''Instantiates a User object
        '''
        self.user = User()

    def test_instance_type(self):
        '''Tests the type of the instance
        '''
        self.assertIs(type(self.user), User)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.user, BaseModel))

    # Test attributes

    def test_email_type(self):
        '''Tests the type of the email attribute
        '''
        self.assertIs(type(self.user.email), str)

    def test_city_id_value(self):
        '''Tests the value of the email attribute
        '''
        self.assertEqual(self.user.email, '')

    def test_password_type(self):
        '''Tests the type of the password attribute
        '''
        self.assertIs(type(self.user.password), str)

    def test_password_value(self):
        '''Tests the value of password
        '''
        self.assertEqual(self.user.password, '')

    def test_first_name_type(self):
        '''Tests the type of the first_name attribute
        '''
        self.assertIs(type(self.user.first_name), str)

    def test_first_name_value(self):
        '''Tests the value of first_name attribute
        '''
        self.assertEqual(self.user.first_name, '')

    def test_last_name_type(self):
        '''Tests the type of the description attribute
        '''
        self.assertIs(type(self.user.last_name), str)

    def test_last_name_value(self):
        '''Tests the value of last_name
        '''
        self.assertEqual(self.user.last_name, '')

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.user.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.user.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.user.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.user.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.user.__class__, User)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[User] ({}) {}'.format(self.user.id, self.user.__dict__)
        self.assertEqual(self.user.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.user.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'User'
        self.assertEqual(self.user.to_dict(), dictionary)
