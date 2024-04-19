#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from models.place import Place
from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
