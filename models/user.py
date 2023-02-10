#!/usr/bin/python3
# User class inherits from BaseModel

from models.base_model import BaseModel


class User(BaseModel):
    '''Defines a User class that inherits from BaseModel class

    Attributes:
        email: user email
        password: user password
        first_name: user first name
        last_name: user last name
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
