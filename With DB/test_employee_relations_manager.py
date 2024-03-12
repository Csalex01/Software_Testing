import unittest
import datetime

from relations_manager import RelationsManager
from models import Employee

class TestEmployeeRelationsManager(unittest.TestCase):

    def setUp(self):
        self.rm = RelationsManager()
        self.employees = self.rm.get_all_employees()

    def test_team_leader_birthday(self):
        john_doe = list(
            filter(
                lambda e: e.first_name == "John" and e.last_name == "Doe", 
                self.employees
            )
        )[0]
            
        self.assertTrue(self.rm.is_leader(john_doe))
        self.assertEqual(john_doe.birth_date, datetime.date(1970, 1, 31))

    def test_team_members(self):
        john_doe = list(
            filter(
                lambda e: e.first_name == "John" and e.last_name == "Doe", 
                self.employees
            )
        )[0]

        team_members = self.rm.get_team_members(john_doe)

        expected_team_members = [2, 3]

        self.assertTrue(expected_team_members, team_members)

    def test_team_member_excluded(self):
        john_doe = list(
            filter(
                lambda e: e.first_name == "John" and e.last_name == "Doe", 
                self.employees
            )
        )[0]

        team_members = self.rm.get_team_members(john_doe)
        tomas_andre_id = 5

        self.assertTrue(tomas_andre_id not in team_members)

    def test_base_salary(self):

        gretchen_watford = list(
            filter(
                lambda e: e.first_name == "Gretchen" and e.last_name == "Watford", 
                self.employees
            )
        )[0]

        self.assertEqual(gretchen_watford.base_salary, 4000)

    def test_not_team_leader(self):
        tomas_andre = list(
            filter(
                lambda e: e.first_name == "Tomas" and e.last_name == "Andre", 
                self.employees
            )
        )[0]

        self.assertFalse(self.rm.is_leader(tomas_andre))
        self.assertEqual(self.rm.get_team_members(tomas_andre), None)