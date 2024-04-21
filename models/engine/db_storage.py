#!/usr/bin/python3
""" A module for database storage """
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """ A class to define how to interact with the database """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialises the database """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the database depending on class name  and return dictionary
        """
        dct = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for _ in query:
                key = f"{type(_).__name__}.{_.id}"
                dct[key] = _

        else:
            classes = [State, City, User, Place, Review, Amenity]
            for clss in classes:
                query = self.__session.query(clss)
                for _ in query:
                    key = f"{type(_).__name__}.{_.id}"
                    dct[key] = _
        return dct

    def new(self, obj):
        """ adds a new element"""
        self.__session.add(obj)

    def save(self):
        """ saves changes to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object from the table """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ Reloads the database """
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """ closes a session """
        self.__session.remove()
