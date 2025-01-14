from db import session
from random import choice, randint
from faker import Faker
from models.groups import Group
from models.students import Student
from models.teachers import Teacher
from models.marks import Mark
from models.subjects import Subject
from datetime import date

GROUPS = ["MCS4", "MDA2", "CS1"]
SUBJECTS = ["Python", "Math", "CSS", "HTML", "JS"]

fake = Faker("uk_UA")


def seed_groups(groups: list) -> None:
    for group in groups:
        new_group = Group(name=group)
        session.add(new_group)
    session.commit()


def seed_subjects(subjects: list) -> None:
    teacher_ids = [x.id for x in session.query(Teacher).all()]
    for subject in subjects:
        new_subject = Subject(name=subject, teacher_id=choice(teacher_ids))
        session.add(new_subject)
    session.commit()


def seed_students(students: int) -> None:
    group_ids = [x.id for x in session.query(Group).all()]

    for i in range(students):
        new_student = Student(
            name=fake.name(), group_id=choice(group_ids), email=fake.email()
        )
        session.add(new_student)
    session.commit()


def seed_teachers(teachers: int) -> None:

    for _ in range(teachers):
        new_teacher = Teacher(name=fake.name())
        session.add(new_teacher)
    session.commit()


def seed_marks(mark_number: int) -> None:
    subject_ids = [x.id for x in session.query(Subject).all()]
    student_ids = [x.id for x in session.query(Student).all()]

    for subject in subject_ids:
        for student in student_ids:
            new_mark = Mark(
                mark=randint(20, 100),
                date=fake.date_between_dates(
                    date_start=date(2024, 10, 1), date_end=date(2024, 12, 31)
                ),
                student_id=student,
                subject_id=subject,
            )
            session.add(new_mark)
    session.commit()


def fill_db():
    seed_groups(GROUPS)
    seed_students(30)
    seed_teachers(5)
    seed_subjects(SUBJECTS)
    seed_marks(20)


if __name__ == "__main__":
    fill_db()