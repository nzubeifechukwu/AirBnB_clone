#!/usr/bin/python3
# This module contains the State class

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    '''State class inherits from BaseModel class

    Attributes:
        name: name of the state
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    @property
    def cities(self):
        '''Gets the cities attributes for FileStorage
        '''
        cities_list = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                cities_list.append(city)
        return cities_list
