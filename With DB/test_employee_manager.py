import unittest

from datetime import date

from employee_manager import EmployeeManager
from relations_manager import RelationsManager

from databse import DB
from models import Employee

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.DB = DB()
        self.rm = RelationsManager(db=self.DB)
        self.em = EmployeeManager(relations_manager=self.rm)
    
    def test_not_team_leader_salary(self):
        employee = self.DB.get_employee(2)

        expected_salary = 3600
        salary = self.em.calculate_salary(employee)

        self.assertEqual(expected_salary, salary)

    def test_team_leader_salary(self):
        leader = Employee(
            id=7,
            first_name="Jane",
            last_name="Doe",
            birth_date=date(1980, 1, 1),
            base_salary=2000,
            hire_date=date(2008, 10, 10)
        )

        self.rm.teams[7] = [8, 9, 10]
        salary = self.em.calculate_salary(leader)

        expected_salary = 3600
        self.assertEqual(expected_salary, salary)

    def test_email_notfication(self):
        employee = Employee(
            id=10,
            first_name="John",
            last_name="Doe",
            birth_date=date(1980, 1, 1),
            base_salary=3000,
            hire_date=date(1998, 10, 10)
        )

        salary = self.em.calculate_salary(employee)
        expected_message = f"{employee.first_name} {employee.last_name} your salary: {salary} has been transferred to you."
        message = self.em.calculate_salary_and_send_email(employee)

        self.assertEqual(expected_message, message)