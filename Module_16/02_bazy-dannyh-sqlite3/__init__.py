from database import *
from random import choice, randint

FIRSTNAME = ['Ivan', 'Ilya', 'Alex', 'Maria', 'Denis']
LASTNAME = ['Pink', 'Black', 'Cyan', 'Red', 'Blue', 'Orange', 'Yellow', 'White']
SUBJECT = ['Python', 'PHP', 'C++', 'JavaScript']


class University:
    def __init__(self, name):
        self.name = name
        check_has_db_and_create(name)
        self.work_with_db = func_work_with_db(name)

    def add_student(self, name, age):
        self.work_with_db(f"INSERT INTO Students (name, age) VALUES ('{name}', '{age}')")

    def add_grade(self, student_id, subject, grade):
        self.work_with_db(f"""INSERT INTO Grades (student_id, subject, grade)
                                VALUES ('{student_id}', '{subject}', '{grade}')""")

    def get_students(self, subject=''):
        if subject:
            subject = f"AND subject = '{subject}'"

        result = self.work_with_db(f"""
        SELECT S.name, S.age, G.subject, G.grade 
        FROM Students as S, Grades as G
        WHERE S.id = student_id {subject} ORDER BY name""")
        return result

    def __len__(self):
        return self.work_with_db(f"SELECT COUNT(id) FROM Students")[0][0]


u1 = University('Urban')

for name in FIRSTNAME:
    u1.add_student(name + ' ' + choice(LASTNAME), randint(20, 30))

for _ in range(2):
    for i in range(len(u1)):
        grade = randint(60, 100) / 20
        u1.add_grade(i + 1, choice(SUBJECT), round(grade, 1))

print(u1.get_students())
print(u1.get_students('Python'))
