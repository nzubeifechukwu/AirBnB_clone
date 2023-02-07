#!/usr/bin/python3
# BaseModel class defines all common attributes/methods for other classes

from datetime import datetime
import uuid


class BaseModel:
    '''Defines common attributes/methods for other classes
    '''

    def __init__(self, id=None, created_at=None, updated_at=None):
        '''Instantiates a BaseModel class

        Args:
            id: String. Unique identifier for the instance. Defaults to None
            created_at: Current datetime when an instance is created
            updated_at: Current datetime when an instance is changed. Updated
                every time the object changes
        '''
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        '''Demonstrates how to print the object
        '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute updated_at
            with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of
            __dict__ of the instance
        '''
        dictionary = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dictionary[k] = v.isoformat()
            else:
                dictionary[k] = v
        dictionary['__class__'] = type(self).__name__
        return dictionary
