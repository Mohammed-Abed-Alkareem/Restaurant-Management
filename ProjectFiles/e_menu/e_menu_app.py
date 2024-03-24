from flask import Flask, render_template, redirect, url_for, request
from utils.db import *
from customers import customers
from managers import managers


app = Flask(__name__)

# Register your blueprints with proper URL prefixes

app.register_blueprint(customers)
app.register_blueprint(managers)

app.secret_key= 'mysecret!!@@'

@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.errorhandler(404)
def not_found(e):
    return ("404 not found"),404


if __name__ == '__main__':
    #reset_db()

    app.run(host='0.0.0.0',port=1111, debug=True)


