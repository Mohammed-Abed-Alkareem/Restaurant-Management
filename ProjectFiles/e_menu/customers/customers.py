from . import customers  # Import the blueprint from the package

from flask import render_template, request, url_for, redirect
from ProjectFiles.e_menu.utils.db import *

=======
from flask import render_template, request, url_for, redirect, session
from e_menu.utils.db import *

from .models import *


@customers.route('/', methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        tbl_code = request.form['tbl_code']

        print(tbl_code)
        table = get_table_by_id(table_id=tbl_code)
        print(table)
        if 'table' in session:
            session.pop('table', None)

        if table is not None:
            session["table"] = table[0] # here it must be the object, [0] is only for now
            session.modified = True
            return redirect(url_for('customers.sign_page'))

    return render_template("customers/home_page.html")


@customers.route('/sign')
def sign_page():
    if 'table' in session and session['table'] is not None:
        return render_template("customers/sign_page.html")

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/sign/sign_up', methods=['POST', 'GET'])
def sign_up():
    if 'table' in session and session['table'] is not None:
        if request.method == 'POST':
            customer_name = request.form['name']
            customer_phone = request.form['phone']

            print(customer_name, customer_phone)

            # check insert_customer(customer_name, customer_phone)
            #if return sucessfully
            #   redirect to log in
            #else
            #   the phone is already registered
            #   display a message that the phone number is already registered
        return render_template("customers/sign_up.html")

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/sign/log_in', methods=['POST', 'GET'])
def log_in():
    if 'table' in session and session['table'] is not None:
        if request.method == 'POST':
            user_phone = request.form['phone']

            print(user_phone)
            customer = 0 #get_customer_by_phone(user_phone=user_phone) #not implemented yet

            session["customer"] = customer
            session.modified = True
            return redirect(url_for('customers.categories'))  #after making log in

        return render_template("customers/log_in.html")

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/categories')
def categories():
   # if 'customer' in session and session['customer'] is not None:
        items_categories = get_menuItems_categories()
        return render_template("customers/categories.html", items_categories=items_categories, user_name='mohammed')#session['customer'].name)

    # else:
    #     return redirect(url_for('customers.home_page'))

@customers.route('/categories/<category>')
def category_items(category):
    #if 'table' in session and session['table'] is not None:
        menuItems = get_menuItems_data(category)

        return render_template("customers/menuItems.html", menuItems=menuItems)

    # else:
    #     return redirect(url_for('customers.home_page'))

@customers.route('categories/<category>/<menu_item>')
def dish_details(category, menu_item):

        dishes = ["burger", "chicken", "meat"]
        return render_template("customers/Details.html", category=category, menu_item = menu_item)

    # else:
    #     return redirect(url_for('customers.home_page'))