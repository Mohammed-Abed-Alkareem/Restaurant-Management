STUDENTS_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
"""

COURSES_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
);
"""

GET_STUDENTS_TABLE = 'SELECT * FROM students'

GET_COURSES_TABLE = 'SELECT * FROM courses'


INSERT_STUDENT = """
INSERT INTO students (name, age) VALUES (?, ?)
"""

INSERT_COURSE = """
INSERT INTO courses (name, student_id) VALUES (?, ?)
"""
