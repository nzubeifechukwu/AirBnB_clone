#!/usr/bin/python3
# User class inherits from BaseModel

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''Defines a User class that inherits from BaseModel class

    Attributes:
        email: user email
        password: user password
        first_name: user first name
        last_name: user last name
    '''
    __tablename__ ='users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
