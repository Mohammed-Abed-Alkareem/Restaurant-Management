from flask import Flask, render_template, redirect, url_for, request
from utils.db import *

app = Flask(__name__)


@app.route('/')
def index():
    students = get_students()
    return render_template('all_students.html', students=students)


@app.route('/student/<int:student_id>')
def student_detail(student_id):
    student = get_student_by_id(student_id)
    if student:
        return render_template('student_detail.html', student=student)
    else:
        return "Student not found."


@app.route('/students', methods=['GET', 'POST'])
def display_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        student = get_student_by_id(student_id)
        if student:
            return render_template('students.html', student=student)
        else:
            return "Student not found."
    return render_template('student_form.html')


@app.route('/courses')
def display_courses():
    courses = get_courses()
    return render_template('courses.html', courses=courses)


@app.route('/osama')
def osmaa():
    return render_template('osama.html')


@app.route('/addstudent', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        std_name = request.form['std_name']
        std_age = request.form['std_age']
        # Values for the new student are taken from the form data
        student_data = (std_name, std_age)
        insert_student(*student_data)
        return redirect(url_for('index'))
    return render_template('add_student_form.html')


# @app.errorhandler(404)
# # inbuilt function which takes error as parameter
# def not_found(e):
#     # defining function
#     return render_template("404.html")


@app.route('/', subdomain='manager')
def practice():
    return "Coding Manager Page"



# if __name__ == '__main__':
#     reset_db()
#     # init_db() #  not now
#     website_host = 'restaurant_e-menu' #  in order to change it must be changed in the DNS File
#     website_port = 1111
#     app.config['SERVER_NAME'] = f"{website_host}:{website_port}"
#     app.run(debug=True)


if __name__ == '__main__':
    reset_db()
    # init_db() #  not now
    app.run(host='0.0.0.0',port=1111, debug=True)