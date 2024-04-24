#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import shlex
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Returns a list of city instances with state_id = State_id"""
            all_data = models.storage.all()
            cities = []
            res = []
            for keys in all_data:
                city = keys.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    cities.append(all_data[keys])

            for _ in cities:
                if (_.state_id == self.id):
                    res.append(_)
            return res
