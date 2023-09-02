#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models import storage_engine, storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, Float,  ForeignKey, Table
from sqlalchemy.orm import relationship


if storage_engine == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place.id", String(60), ForeignKey(
               onupdate="CASCADE", ondelete="CASCADE"
               ), primary_key=True),
        Column("amenity_id", String(60), ForeignKey(
            "amenities.id", onupdate="CASCADE",
            ondelete="CASCADE"), primary_key=True
        ))

class Place(BaseModel, Base):
    """ A place to stay """
    if storage_engine == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0)
        longitude = Column(Float, nullable=False, default=0)
        review = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
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
        review = ""
        amenities = ""

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

        @property
        def reviews(self):
            """Get list of reviews in relation with place"""
            place_reviews = []
            reviews_data = storage.all(City)
            for review in reviews_data.values():
                if review.place_id == self.id:
                    place_reviews.append(review)
            return place_reviews
