from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from typing import List

Base = declarative_base()

class Employees(Base):
    __tablename__ = "employees"

    employeeId = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    birthDate = Column(Date)
    baseSalary = Column(Integer)
    hireDate = Column(Date)
    team_id = Column(Integer, ForeignKey("teams.teamId"))
    team = relationship("Teams", back_populates="members")

class Teams(Base):
    __tablename__ = "teams"

    teamId = Column(Integer, primary_key=True)
    leaderId = Column(Integer)
    mebers = relationship("Employees", back_populates="team", cascade="all, delete-orphan")