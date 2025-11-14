from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from datetime import datetime

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    team = Column(String)
    country = Column(String)
    points = Column(Float)
    wins = Column(Integer)
    podiums = Column(Integer)
    pole_positions = Column(Integer)
    fastest_laps = Column(Integer)
    championships = Column(Integer)
    grand_chelem = Column(Integer)

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    year_founded = Column(String) #Formato YYYY
    points = Column(Float)
    team_principal = Column(String)

class GrandPrix(Base):
    __tablename__ = "grand_prix"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    id_track_name = Column(Integer, ForeignKey("tracks.id"))
    track_name = Column(String)
    date_event = Column(String) #Formato DD/MM/YYYY to DD/MM/YYYY
    fastest_lap = Column(String)
    fastest_driver = Column(String)
    fastest_lap_year = Column(String)
    id_driver = Column(Integer, ForeignKey("drivers.id"))
    id_team = Column(Integer, ForeignKey("teams.id"))
    winner_driver = Column(String)
    podium_2 = Column(String)
    podium_3 = Column(String)
    winner_team = Column(String)
    poleman = Column(String)
    pole_team = Column(String)
    pole_time = Column(String) #Formato MM:SS:MS
    qualification_result = Column(String) #Formato JSON
    grid = Column(String) #Formato JSON
    race_results = Column(String) #Formato JSON
    date = Column(String)
    weekend_sprint = Column(bool)
    sprint_shotout_man = Column(String) #Piloto mas rapido en la sesion sprint shotout
    sprint_shotout_lap = Column(String) #Tiempo del piloto mas rapido en la sesion sprint shotout
    sprint_shotout_result = Column(String) #Formato JSON
    sprint_grid = Column(String) #Formato JSON
    sprint_winner = Column(String)
    sprint_podium_2 = Column(String)
    sprint_podium_3 = Column(String)
    sprint_winner_team = Column(String)


class Track(Base)   :
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    year = Column(String) #Formato YYYY
    length_km = Column(Float)
    number_of_laps = Column(Integer)
    lap_record_time = Column(String) #Formato MM:SS:MS
    lap_record_driver = Column(String)
    lap_record_year = Column(String)

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    id_team = Column(Integer, ForeignKey("teams.id"))
    id_chasis = Column(Integer, ForeignKey("chassis.id"))
    id_engine = Column(Integer, ForeignKey("engines.id"))
    id_pneumatics = Column(Integer, ForeignKey("pneumatics.id"))
    team = Column(String)
    chasis = Column(String)
    engine = Column(String)
    weight_kg = Column(Float)
    pneumatics = Column(String)
    designer = Column(String) #Persona responsable del diseño del coche

class Chasis(Base):
    __tablename__ = "chassis"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    material = Column(String)
    suspension_type = Column(String)
    year_introduced = Column(String) #Formato YYYY
    designer = Column(String) #Persona responsable del diseño del chasis

class Engine(Base):
    __tablename__ = "engines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String) #Ejemplo: V6 Turbo Hybrid
    angle_configuration = Column(String) #Ejemplo: 90 degrees
    cylinders = Column(Integer)
    aspiration = Column(String) #Ejemplo: Turbocharged
    cooling_system = Column(String) #Ejemplo: Liquid-cooled
    transmission = Column(String) #Ejemplo: 8-speed semi-automatic
    type_transmission = Column(String) #Ejemplo: Sequential
    transmission_axle = Column(String) #Ejemplo: Rear-wheel drive    manufacturer = Column(String)
    year_introduced = Column(String) #Formato YYYY
