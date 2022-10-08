#!/usr/bin/python3
"""
python file that contains the class definition of Cities
and an instance Base = declarative_base()
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """the City class linked to the declarative_base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)