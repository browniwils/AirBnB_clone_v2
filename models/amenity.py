#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sql


class Amenity(BaseModel, Base):
    """
    Model amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
