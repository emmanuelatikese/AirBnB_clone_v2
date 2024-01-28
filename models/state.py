#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    @property
    def cities(self):
        from models import storage
        cities = storage.all(City)
        states_cities = []

        for x in cities.values():
            if x.state_id == self.id:
                states_cities.append(x)
        return states_cities
