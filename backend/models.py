from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    team = Column(String)
    country = Column(String)
    points = Column(Float)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    points = Column(Float)