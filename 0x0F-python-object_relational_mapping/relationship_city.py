#!/usr/bin/python3
"""
Defines City class to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    __tablename__: The table name of the class
        id: The id of the class
        name: The name of the class
        state: The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
