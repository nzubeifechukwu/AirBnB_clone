#!/usr/bin/python3
# BaseModel class defines all common attributes/methods for other classes

from datetime import datetime
import uuid
import models


class BaseModel:
    '''Defines common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''Instantiates a BaseModel class

        Attributes:
            id: String. Unique identifier for the instance. Defaults to None
            created_at: Current datetime when an instance is created
            updated_at: Current datetime when an instance is changed. Updated
                every time the object changes
        '''
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        models.storage.save()

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
