from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session
from typing import List

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    base_salary = Column(Integer)
    hire_date = Column(Date)
    team_id = Column(Integer, ForeignKey("team.id"), nullable=True)
    team = relationship("Team", back_populates="members")


class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)
    leader_id = Column(Integer)
    members = relationship("Employee", back_populates="team", cascade="all, delete-orphan")