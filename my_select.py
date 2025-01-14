from sqlalchemy import func
from db import session
from random import choice, randint
from faker import Faker
from models.groups import Group
from models.students import Student
from models.teachers import Teacher
from models.marks import Mark
from models.subjects import Subject
from datetime import date


def select_1():
    result = (
        session.query(Student.name, func.avg(Mark.mark))
        .join(Mark, Student.id == Mark.student_id)
        .group_by(Student.name)
        .order_by(func.avg(Mark.mark).desc())
        .limit(5)
        .all()
    )

    return result


def select_2(subject_name):
    result = (
        session.query(Student.name, func.avg(Mark.mark))
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Mark.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.name)
        .order_by(func.avg(Mark.mark).desc())
        .limit(1)
        .all()
    )
    return result


def select_3(subject_name):
    result = (
        session.query(Group.name, func.avg(Mark.mark))
        .join(Student, Student.group_id == Group.id)
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Mark.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.name)
        .order_by(Group.name)
        .all()
    )
    return result


def select_4():
    result = session.query(func.avg(Mark.mark)).scalar()
    return result


def select_5(teacher_name):
    result = (
        session.query(Subject.name)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Teacher.name == teacher_name)
        .all()
    )
    return result


def select_6(group_name):
    result = (
        session.query(Student.name)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    return result


def select_7(group_name, subject_name):
    result = (
        session.query(Student.name, Mark.mark)
        .join(Group, Student.group_id == Group.id)
        .join(Mark, Student.id == Mark.student_id)
        .join(Subject, Mark.subject_id == Subject.id)
        .filter(Group.name == group_name)
        .filter(Subject.name == subject_name)
        .all()
    )
    return result


def select_8(teacher_name):
    result = (
        session.query(func.avg(Mark.mark))
        .join(Subject, Mark.subject_id == Subject.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Teacher.name == teacher_name)
        .scalar()
    )
    return result


def select_9(student_name):
    result = (
        session.query(Subject.name)
        .join(Mark, Subject.id == Mark.subject_id)
        .join(Student, Mark.student_id == Student.id)
        .filter(Student.name == student_name)
        .all()
    )
    return result


def select_10(student_name, teacher_name):
    result = (
        session.query(Subject.name)
        .join(Mark, Subject.id == Mark.subject_id)
        .join(Student, Mark.student_id == Student.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .filter(Student.name == student_name)
        .filter(Teacher.name == teacher_name)
        .all()
    )
    return result


def select():
    print(select_1())
    print(select_2("Math"))
    print(select_3("HTML"))
    print(select_4())
    print(select_5("Анжела Акуленко"))
    print(select_6("MDA2"))
    print(select_7("MDA2", "Python"))
    print(select_8("Віра Гавриленко"))
    print(select_9("Мирослав Дурдинець"))
    print(select_10("Мирослав Дурдинець", "Віра Гавриленко"))


if __name__ == "__main__":
    print(select())
