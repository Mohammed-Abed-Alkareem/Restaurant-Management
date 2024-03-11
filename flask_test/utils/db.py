import sqlite3
from .queries import *

DATABASE = 'database.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(STUDENTS_CREATE_TABLE)
    cursor.execute(COURSES_CREATE_TABLE)

    conn.commit()
    conn.close()


def reset_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS students;")
    cursor.execute("DROP TABLE IF EXISTS courses;")

    # Recreate tables
    cursor.execute(STUDENTS_CREATE_TABLE)
    cursor.execute(COURSES_CREATE_TABLE)

    # Add initial values
    cursor.execute("INSERT INTO students (name, age) VALUES ('Mohammed', 21);")
    cursor.execute("INSERT INTO students (name, age) VALUES ('Mosa', 22);")
    cursor.execute("INSERT INTO students (name, age) VALUES ('Osama', 10);")


    conn.commit()
    conn.close()

def get_students():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(GET_STUDENTS_TABLE)
        return cursor.fetchall()


def get_courses():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(GET_COURSES_TABLE)
        return cursor.fetchall()


def insert_student(name, age):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_STUDENT, (name, age))
        conn.commit()


def insert_course(name, student_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_COURSE, (name, student_id))
        conn.commit()

def get_student_by_id(student_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Assuming 'students' table structure: (id, name, age)
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    connection.close()

    return student