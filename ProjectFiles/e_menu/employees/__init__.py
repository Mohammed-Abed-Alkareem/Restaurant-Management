from flask import Blueprint

employees = Blueprint('employees', __name__, url_prefix='/manager')

from .employees import *  # Import routes from manager.py
