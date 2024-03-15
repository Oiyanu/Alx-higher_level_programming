#!/usr/bin/python3
"""contains the class definition of a state and an instance Base"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullabale=False, unique=True)
    name = Column(String(128), nullable=False)
