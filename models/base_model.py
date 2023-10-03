#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage_engine, storage
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if storage_engine == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""
    if storage_engine == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    else:
        id = str(uuid.uuid4())
        created_at = datetime.utcnow()
        updated_at = created_at
        
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        try:
                            setattr(self, key, datetime.fromisoformat(val))
                        except ValueError as err:
                            pass
                    else:
                        setattr(self, key, val)

                    if key == "id" and val is not None:
                        setattr(self, key, str(uuid.uuid4()))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Delete current instance from storage"""
        storage.delete(self)
