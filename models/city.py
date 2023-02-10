#!/usr/bin/python3
# This module contains the City class

from models.base_model import BaseModel


class City(BaseModel):
    '''City class inherits from BaseModel class

    Attributes:
        state_id: empty string (will eventually be set to State.id)
        name: city name
    '''
    state_id = ''
    name = ''
