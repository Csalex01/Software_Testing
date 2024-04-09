import unittest

from datetime import date

from employee_manager import EmployeeManager
from relations_manager import RelationsManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databse import DB
from models import Employee

class TestEmployeeManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///employees.db")
        session = sessionmaker(bind=cls.engine)
        cls.session = session()

    def setUp(self):
        
        self.rm = RelationsManager(session=self.session)
        self.em = EmployeeManager(relations_manager=self.rm)
    
    def test_not_team_leader_salary(self):
        employee = self.session.query(Employee).filter_by(first_name="Tomas").first()
        self.assertIsNotNone(employee, "Employee does not exist in the database")

        calculated_salary = self.em.calculate_salary(employee)
        expected_salary = 2500

        self.assertEqual(expected_salary, calculated_salary)

    def test_team_leader_salary(self):
        leader = self.session.query(Employee).filter_by(first_name="Gretchen").first()
        self.assertIsNotNone(leader, "Team Leader does not exist in the database")

        calculated_salary = self.em.calculate_salary(leader)
        expected_salary = 7400

        self.assertEqual(expected_salary, calculated_salary)

    def test_email_notification(self):
        employee = self.session.query(Employee).filter(Employee.id == 1).first()

        salary = self.em.calculate_salary(employee)
        expected_message = f"{employee.first_name} {employee.last_name} your salary: {salary} has been transferred to you."
        message = self.em.calculate_salary_and_send_email(employee)

        self.assertEqual(expected_message, message)