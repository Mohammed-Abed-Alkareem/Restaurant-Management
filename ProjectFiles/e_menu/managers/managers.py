from flask import render_template, request

from . import managers  # Import the blueprint from the package

@managers.route("/")
def home_page():
    return render_template ("managers/home_page.html")

@managers.route('/gettablecode', methods=['POST', 'GET'])
def manager_login():
    if request.method == 'POST':
        usr_name = request.form['usr_name']
        password = request.form['password']
        print(usr_name)
        print(password)


    return render_template("managers/home_page.html")