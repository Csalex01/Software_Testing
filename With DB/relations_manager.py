import datetime

from models import Employee, Team
from databse import DB

class RelationsManager:
    def __init__(self, session=None):
        self.session = session
        self.employee_list = self.session.query(Employee).all()
        self._teams = self.session.query(Team).all()

        self.teams = {}
        for team in self._teams:
            self.teams[team.leader_id] = team.members

    def is_leader(self, employee) -> bool:
        return employee.id in self.teams

    def get_all_employees(self) -> list:
        return self.employee_list

    def get_team_members(self, employee: Employee) -> list:
        if self.is_leader(employee):
            member_ids = self.teams[employee.id]
            members = [e.id for e in self.employee_list if e.id in member_ids]

            return members
