#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_engine
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Model amenity
    """
    if storage_engine == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
        place_amenities = ""

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
