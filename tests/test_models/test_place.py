#!/usr/bin/python3
# Unit Test for the Place class

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestAmenity(unittest.TestCase):
    '''Tests the City class
    '''

    def setUp(self):
        '''Instantiates a Place object
        '''
        self.place = Place()

    def test_instance_type(self):
        '''Tests the type of a Place instance
        '''
        self.assertIs(type(self.place), Place)

    def test_inheritance(self):
        '''Tests if the instance inherits from a BaseModel
        '''
        self.assertTrue(isinstance(self.place, BaseModel))

    # Test attributes

    def test_city_id_type(self):
        '''Tests the type of the city_id attribute
        '''
        self.assertIs(type(self.place.city_id), str)

    def test_city_id_value(self):
        '''Tests the value of the city_id attribute
        '''
        self.assertEqual(self.place.city_id, '')

    def test_user_id_type(self):
        '''Tests the type of the user_id attribute
        '''
        self.assertIs(type(self.place.user_id), str)

    def test_user_id_value(self):
        '''Tests the value of user_id
        '''
        self.assertEqual(self.place.user_id, '')

    def test_name_type(self):
        '''Tests the type of the name attribute
        '''
        self.assertIs(type(self.place.name), str)

    def test_name_value(self):
        '''Tests the value of name attribute
        '''
        self.assertEqual(self.place.name, '')

    def test_description_type(self):
        '''Tests the type of the description attribute
        '''
        self.assertIs(type(self.place.description), str)

    def test_description_value(self):
        '''Tests the value of description
        '''
        self.assertEqual(self.place.description, '')

    def test_number_rooms_type(self):
        '''Tests the type of the number_rooms attribute
        '''
        self.assertIs(type(self.place.number_rooms), int)

    def test_number_rooms_value(self):
        '''Tests the value of number_rooms
        '''
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_type(self):
        '''Test the type of number_bathrooms
        '''
        self.assertIs(type(self.place.number_bathrooms), int)

    def test_number_bathrooms_value(self):
        '''Tests the value of number_bathrooms
        '''
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_type(self):
        '''Tests the type of max_guest
        '''
        self.assertIs(type(self.place.max_guest), int)

    def test_max_guest_value(self):
        '''Tests the value of max_guest
        '''
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_type(self):
        '''Tests the type of price_by_night
        '''
        self.assertIs(type(self.place.price_by_night), int)

    def test_price_by_night_value(self):
        '''Tests the value of price_by_night
        '''
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_type(self):
        '''Tests the type of latitude
        '''
        self.assertIs(type(self.place.latitude), float)

    def test_latitude_value(self):
        '''Tests the value of latitude
        '''
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_type(self):
        '''Tests the type of longitude
        '''
        self.assertIs(type(self.place.longitude), float)

    def test_longitude_value(self):
        '''Tests the value of longitude
        '''
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_type(self):
        '''Tests the type of amenity_ids
        '''
        self.assertIs(type(self.place.amenity_ids), list)

    def test_amenity_ids_value(self):
        '''Tests the value of amenity_ids
        '''
        self.assertEqual(self.place.amenity_ids, [])

    def test_id_type(self):
        '''Tests type of id attribute
        '''
        self.assertIs(type(self.place.id), str)

    def test_created_at_type(self):
        '''Tests type of attribute created_at
        '''
        self.assertIs(type(self.place.created_at), datetime)

    def test_updated_at_type(self):
        '''Tests type of updated_at attribute
        '''
        self.assertIs(type(self.place.updated_at), datetime)

    def test_class_type(self):
        '''Tests type of __class__ attribute
        '''
        self.assertIs(type(self.place.__class__), type)

    def test_class_value(self):
        '''Tests the value of the __class__ attribute
        '''
        self.assertEqual(self.place.__class__, Place)

    # Test instance methods

    def test_str(self):
        '''Tests the __str__ method
        '''
        f = '[Place] ({}) {}'.format(self.place.id, self.place.__dict__)
        self.assertEqual(self.place.__str__(), f)

    def test_to_dict(self):
        '''Tests the to_dict method
        '''
        dictionary = {}
        for k, v in self.place.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = 'Place'
        self.assertEqual(self.place.to_dict(), dictionary)
