#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel):
    __tablename__ = 'amenities'
    if getenv('') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
