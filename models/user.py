#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models import storage_engine, storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if storage_engine == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
