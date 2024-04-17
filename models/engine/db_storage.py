#!/usr/bin/python3
"""db"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialise"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine(
            f'mysql://{user}:{password}@{host}:3306/{database}',
            pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        # if cls is not None:
        #     self.__session = scoped_session(sessionmaker(bind=self.__engine))
        #     return self.__session.query(cls).all()
        # else:
        #     result = {}
        #     for i in Base.__subclasses__():  # Retrieves all the
        #         # subclasses of the Base class
        #         for obj in self.__session.query(i).all():
        #             result.update('{}.{}'.format(obj, obj.id))
        #     return result
        my_classes = (Amenity, City, Place, Review, State, User)
        objects = dict()

        if cls is None:
            for item in my_classes:
                query = self.__session.query(item)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj
        return objects

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)

        my_session_maker = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        my_session = scoped_session(my_session_maker)
        self.__session = my_session()

    def close(self):
        """close the query"""
        self.__session.close()
