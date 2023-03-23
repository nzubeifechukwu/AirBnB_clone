#!/usr/bin/python3
# This module contains the City class

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class City(BaseModel, Base):
    '''City class inherits from BaseModel class

    Attributes:
        state_id: empty string (will eventually be set to State.id)
        name: city name
    '''
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
