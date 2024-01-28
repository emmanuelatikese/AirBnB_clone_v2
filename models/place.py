#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
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
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        '''another review'''
        rev_all, lt = storage.all(Review), []
        lt = [x for x in rev_all.values()
              if x.place_id == self.id]
        return lt

    @property
    def amenities(self):
        '''This amenities'''
        from models import storage
        amen_all, lt = storage.all(Amenity), []
        lt = [x for x in amen_all.values()
              if x in self.amenity_ids]
        return lt

    @amenities.setter
    def amenities(self, obj):
        '''this is a method'''
        if obj is not None:
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
