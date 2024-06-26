from flask import Flask, render_template

from ProjectFiles.e_menu.customers import customers
from ProjectFiles.e_menu.employees import employees

from ProjectFiles.e_menu.utils.db import reset_db

app = Flask(__name__)

# Register blueprints with proper URL prefixes

app.register_blueprint(customers)
app.register_blueprint(employees)

app.secret_key = 'mysecret!!@@'


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.errorhandler(404)
def not_found(e):
    return ("404 not found"), 404


if __name__ == '__main__':
    # reset_db()

    app.run(host='0.0.0.0', port=1111, debug=True)
