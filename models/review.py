#!/usr/bin/python3
# This module contains the Review class

from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class inherits from BaseModel class

    Attributes:
        place_id: string (will later be set to Place.id)
        user_id: string (will later be set to User.id)
        text: string
    '''
    place_id = ''
    user_id = ''
    text = ''
