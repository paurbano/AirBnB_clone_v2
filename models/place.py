#!/usr/bin/python3
"""This is the place class"""
import models
from os import getenv
# from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Relationship Many-Many for task 10
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


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
    # Condition required for task 9
    # if getenv("HBNB_TYPE_STORAGE") == "db":
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
    amenity_ids = []
    # Condition for task 9
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # added for task 9
        # relation with class-table Reviews
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        # added for task 10
        # relation with table/class place_amenity
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
    else:
        # Condition for task 9
        # if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ getter: return list of reviews"""
            list_reviews = []
            dic_reviews = models.storage.all(Review)
            for review in dic_reviews.values():
                # for review in self.reviews:
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        # methods getter and setter for task 10
        @property
        def amenities(self):
            """ Getter: return list of Amenity linked to a Place """
            list_amenities = []
            # dic_amenities = models.storage.all(models.amenity.Amenity)
            objs_ = models.storage.all(Amenity)
            for key, value in objs_.items():
                if value.id in self.amenity_ids:
                    list_amenities.append(value)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """ setter method"""
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
