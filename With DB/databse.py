import sqlalchemy

from os import path

# class DB:

#     __instance = None

#     def __init__(self):
#         if DB.__instance is not None:
#             raise Exception("This class is a singleton!")
#         else:
#             DB.__instance = self

#         self.engine = None
#         self.connection = None
#         self.metadata = None
#         self.DB_NAME = "employees.db"

#     def get_instance(self):
#         return self.__instance

#     def connect_database(self):
#         self.engine = sqlalchemy.create_engine(f'sqlite:///{self.DB_NAME}', echo=True)
#         self.metadata = sqlalchemy.MetaData()
#         self.connection = self.engine.connect()

#     def init_database(self):

#         self.metadata.create_all(self.engine)

from sqlalchemy import create_engine
from models import Base

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

    def get_instance(self):
        return self.__instance

    def connect_database(self):
        self.engine = create_engine(f"sqlite:///{self.DB_NAME}", echo=True)
        self.metadata = Base.metadata  # Associate metadata with the engine
        self.metadata.bind = self.engine
        self.connection = self.engine.connect()

    def init_database(self):
        Base.metadata.create_all(self.engine)