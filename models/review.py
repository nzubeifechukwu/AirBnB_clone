#!/usr/bin/python3
# This module contains the Review class

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    '''Review class inherits from BaseModel class

    Attributes:
        place_id: string (will later be set to Place.id)
        user_id: string (will later be set to User.id)
        text: string
    '''
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    text = Column(String(1024), nullable=False)
