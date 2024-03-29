from flask import Blueprint

customers = Blueprint('customers', __name__, url_prefix="/customer")

from .customers import customers
