#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
import os
from sqlalchemy.orm import relationship
#from models.review import Review

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                    primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                    primary_key=True, nullable=False))

    env = os.getenv('HBNB_TYPE_STORAGE')
    if env == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            " Returns a list of all review instances"
            from models import storage
            from models.review import Review
            all_reviews = storage.all(Review)
            reviews = []

            for k, v in all_reviews:
                if v.get('place_id') == Place.id:
                    reviews.append(v)
            return reviews

        @property
        def amenities(self):
            "Returns a list of amenities based on amenity_id "
            from models import storage
            from models.amenity import Amenity
            all_amenities = storage.all(Amenity)
            amenity_lst = []
            for k, v in all_amenities:
                if v.get('place_id') == Place.id:
                    amenity_lst.append(v)
            return amenity_lst

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute for amenities """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
