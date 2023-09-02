#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models import storage_engine, storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    if storage_engine == "db":
        __table__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if storage_engine != "db":
        @property
        def cities(self):
            """Get list of cities in relation with state"""
            state_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
