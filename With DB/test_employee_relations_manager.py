import unittest
import datetime

from relations_manager import RelationsManager
from models import Employee

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestEmployeeRelationsManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("sqlite:///employees.db")
        session = sessionmaker(bind=cls.engine)
        cls.session = session()

    def setUp(self):

        self.rm = RelationsManager(session=self.session)

    def test_team_leader_birthday(self):
        john_doe = self.session.query(Employee).filter_by(first_name="John", last_name="Doe").first()
            
        self.assertTrue(self.rm.is_leader(john_doe))
        self.assertEqual(john_doe.birth_date, datetime.date(1970, 1, 31))

    def test_team_members(self):
        john_doe = self.session.query(Employee).filter_by(first_name="John", last_name="Doe").first()

        team_members = self.rm.get_team_members(john_doe)
        expected_team_members = [2, 3]

        self.assertTrue(expected_team_members, team_members)

    def test_team_member_excluded(self):
        john_doe = self.session.query(Employee).filter_by(first_name="John", last_name="Doe").first()

        team_members = self.rm.get_team_members(john_doe)
        tomas_andre_id = 5

        self.assertTrue(tomas_andre_id not in team_members)

    def test_base_salary(self):

        gretchen_watford = self.session.query(Employee).filter_by(first_name="Gretchen", last_name="Watford").first()

        self.assertEqual(gretchen_watford.base_salary, 4000)

    def test_not_team_leader(self):
        tomas_andre = self.session.query(Employee).filter_by(first_name="Tomas", last_name="Andre").first()

        self.assertFalse(self.rm.is_leader(tomas_andre))
        self.assertEqual(self.rm.get_team_members(tomas_andre), None)