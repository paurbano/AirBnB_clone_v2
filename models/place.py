#!/usr/bin/python3
"""This is the place class"""
from os import getenv
from models.base_model import BaseModel
from models.review import Review, Base
from sqlalchemy import Column,  Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # Condition required for task 9
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
    else:
        @property
        def reviews(self):
            list_reviews = []
            dic_reviews = models.Storage.all(Review)
            for review in dic_reviews.items():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews
