from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base

from sqlalchemy.orm import sessionmaker

from models import Employee, Team
class DB:

    def __init__(self, session=None):

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
        self.session = sessionmaker(bind=self.engine)
        self.connection = self.engine.connect()

    def init_database(self):
        Base.metadata.create_all(self.engine)

    def close_database(self):
        self.connection.close()
        self.engine.dispose()

    def insert_employee(self, employee):
        self.session.add(employee)
        self.session.commit()

    def insert_employees(self, employees):
        self.session.add_all(employees)
        self.session.commit()

    def get_employees(self):
        return self.session.query(Employee).all()

    def get_employee(self, id):
        return self.session.query(Employee).filter(Employee.id == id).first()

    def insert_team(self, team):
        self.session.add(team)
        self.session.commit()

    def insert_teams(self, teams):
        self.session.add_all(teams)
        self.session.commit()

    def get_teams(self):
        return self.session.query(Team).all()

    def get_team(self, id):
        return self.session.query(Team).filter(Team.id == id).first()
    
    def get_session(self):
        return Session(self.engine)