from flask import Blueprint

managers = Blueprint('managers', __name__, url_prefix='/manager')

from .managers import *  # Import routes from manager.py
