#!/usr/bin/python3
# This module contains the Place class

from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    '''Place class inherits from BaseModel class

    Attributes:
        city_id: string (will eventually be set to City.id)
        user_id: string (will eventually be set to User.id)
        name: string
        description: string
        number_rooms: integer
        number_bathrooms: integer
        max_guest: integer
        price_by_night: integer
        latitude: float
        longitude: float
        amenity_ids: list of string (will later be set to list of Amenity.id)
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    reviews = relationship('Review', backref='place')

    @property
    def reviews(self):
        '''Returns a list of Review instances with place_id equal to Place.id
        '''
        reviews_list = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
