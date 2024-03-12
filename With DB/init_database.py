import datetime

from databse import DB
from models import Employee, Team


def main():
    db = DB()
    db.connect_database()
    db.init_database()

    employee_list = [
        Employee(id=1, first_name="John", last_name="Doe", base_salary=3000,
                    birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1990, 10, 1)),

        Employee(id=2, first_name="Myrta", last_name="Torkelson", base_salary=1000,
                    birth_date=datetime.date(1980, 1, 1), hire_date=datetime.date(2000, 1, 1)),

        Employee(id=3, first_name="Jettie", last_name="Lynch", base_salary=1500,
                    birth_date=datetime.date(1987, 1, 1), hire_date=datetime.date(2015, 1, 1)),

        Employee(id=4, first_name="Gretchen", last_name="Watford", base_salary=4000,
                    birth_date=datetime.date(1960, 1, 1), hire_date=datetime.date(1990, 1, 1)),

        Employee(id=5, first_name="Tomas", last_name="Andre", base_salary=1600,
                    birth_date=datetime.date(1995, 1, 1), hire_date=datetime.date(2015, 1, 1)),

        Employee(id=6, first_name="Scotty", last_name="Bomba", base_salary=1300,
                    birth_date=datetime.date(1977, 1, 1), hire_date=datetime.date(2008, 1, 1))
    ]

    teams = {
        1: [2, 3],
        4: [5, 6]
    }

    db.insert_employees(employee_list)
    
    for idx, team in enumerate(teams):
        team = Team(leader_id=team)

        for member in teams[team.leader_id]:
            team.members.append(db.get_employee(member))

        db.insert_team(team)
        

if __name__ == "__main__":
    main()