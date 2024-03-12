from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base

from models import Employee, Team
class DB:
    __instance = None

    def __init__(self):
        if DB.__instance is not None:
            raise Exception("This class is Singleton!")
        else:
            DB.__instance = self

        self.engine = None
        self.connection = None
        self.metadata = None
        self.DB_NAME = "employees.db"

        self.connect_database()

    def get_instance(self):
        return self.__instance

    def connect_database(self):
        self.engine = create_engine(f"sqlite:///{self.DB_NAME}", echo=True)
        self.metadata = Base.metadata  # Associate metadata with the engine
        self.metadata.bind = self.engine
        self.connection = self.engine.connect()

    def init_database(self):
        Base.metadata.create_all(self.engine)

    def close_database(self):
        self.connection.close()
        self.engine.dispose()

    def insert_employee(self, employee):
        with Session(self.engine) as session:
            session.add(employee)
            session.commit()

    def insert_employees(self, employees):
        with Session(self.engine) as session:
            session.add_all(employees)
            session.commit()

    def get_employees(self):
        with Session(self.engine) as session:
            return session.query(Employee).all()

    def get_employee(self, id):
        with Session(self.engine) as session:
            return session.query(Employee).filter(Employee.id == id).first()

    def insert_team(self, team):
        with Session(self.engine) as session:
            session.add(team)
            session.commit()

    def insert_teams(self, teams):
        with Session(self.engine) as session:
            session.add_all(teams)
            session.commit()

    def get_teams(self):
        with Session(self.engine) as session:
            return session.query(Team).all()

    def get_team(self, id):
        with Session(self.engine) as session:
            return session.query(Team).filter(Team.id == id).first()
    