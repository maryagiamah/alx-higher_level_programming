#!/usr/bin/python3
"""
    A python file that contains the class definition of
    a State and an instance Base = declarative_base()

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """States ORM Class """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref=backref('state', cascade='all'))
