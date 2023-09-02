#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models import storage_engine, storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, Float,  ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    if storage_engine == "db":
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
