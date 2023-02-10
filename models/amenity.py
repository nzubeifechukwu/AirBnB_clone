#!/usr/bin/python3
# This module contains the Amenity class

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity class inherits from BaseModel class

    Attributes:
        name: name of amenity instance
    '''
    name = ''
