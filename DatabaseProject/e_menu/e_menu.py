from flask import Flask, render_template, redirect, url_for, request
from utils.db import *

app = Flask(__name__)


@app.route('/')
def index():
    students = get_students()
    return render_template('all_students.html', students=students)


# @app.errorhandler(404)
# # inbuilt function which takes error as parameter
# def not_found(e):
#     # defining function
#     return render_template("404.html")





if __name__ == '__main__':
    reset_db()
    # init_db() #  not now
    app.run(host='0.0.0.0',port=1111, debug=True)