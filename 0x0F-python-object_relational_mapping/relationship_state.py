#!/usr/bin/python3
"""definition of the state class with relationship to City"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalhemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullabale=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                            cascade='all, delete-orphan')
