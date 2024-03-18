#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(UUID(as_uuid=True), primary_key = True, default=uuid.uuid4,
            nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(),
            nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),
            nullable=False)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'id' not in kwargs.keys():
                kwargs['id'] = str(uuid.uuid4())
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            for k, v in kwargs.items():
                setattr(self, k, v)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
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
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Deletes the current instance of storage"""
        from models import storage
        models.storage.delete(self)
