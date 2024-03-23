from . import customers  # Import the blueprint from the package
from flask import render_template, request, url_for, redirect
from ProjectFiles.e_menu.utils.db import *

from .models import *

@customers.route('/')
def home_page():
    return render_template("customers/home_page.html")


@customers.route('/gettablecode', methods=['POST', 'GET'])
def get_table_code():
    if request.method == 'POST':
        tbl_code = request.form['tbl_code']
        print(tbl_code)
        table = get_table_by_id(table_id=tbl_code)
        if table is None:
            return "not found"
        else:
            # Table found, redirect to the sign page
            return redirect(url_for('customers.sign_page'))

    return render_template("customers/home_page.html")


@customers.route('/sign')
def sign_page():
    return render_template("customers/sign_page.html")

@customers.route('/sign/log_in')
def log_in():
    return render_template("customers/log_in.html")

@customers.route('/sign/sign_up')
def sign_up():
    return render_template("customers/sign_up.html")


@customers.route('<user_name>/categories/')
def categories(user_name):
    items_categories = get_menuItems_categories()
    return render_template("customers/categories.html", items_categories=items_categories, user_name=user_name)


@customers.route('<user_name>/categories/<category>')
def category_items(user_name, category):
    menuItems = get_menuItems_data(category)

    return render_template("customers/menuItems.html", menuItems=menuItems)

@customers.route('<user_name>/categories/<category>/<menu_item>')
def dish_details(user_name, category, menu_item):
    dishes = ["burger", "chicken", "meat"]
    return render_template("customers/Details.html",user_name=user_name, category=category, menu_item = menu_item)