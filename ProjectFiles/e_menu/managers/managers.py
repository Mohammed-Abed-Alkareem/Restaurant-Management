from flask import render_template, request

from . import managers  # Import the blueprint from the package

@managers.route("/")
def home_page():
    return render_template ("managers/home_page.html")
