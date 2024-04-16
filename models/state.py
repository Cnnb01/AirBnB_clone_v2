#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter property"""
        from models import storage
        rel_cities = []
        cities = storage.all(City)
        for i in cities.values():
            if i.state_id == self.id:
                rel_cities.append(i)
        return rel_cities
