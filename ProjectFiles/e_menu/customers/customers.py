from . import customers  # Import the blueprint from the package

import json
from ProjectFiles.e_menu.utils.db import *

from flask import render_template, request, url_for, redirect, session

from .models.tables_model import *
from .models.customers_model import *
from .models.menuItems_model import *

from .models import *



@customers.route('/', methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        table_code = request.form['tbl_code']


        table = Table.get(table_code=table_code)

        if 'table' in session:
            session.pop('table', None)

        if table is not None:
            session["table"] = table.to_dict() #json.dumps(table.__dict__) # here it must be the object, [0] is only for now
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

            check = Customer.insert(Customer(customer_name , customer_phone))

            # check insert_customer(customer_name, customer_phone)
            if check :
                return redirect(url_for('customers.log_in'))
            #   redirect to log in
            else: ## must maje a message flash
                return redirect(url_for('customers.sign_up'))

            #   the phone is already registered
            #   display a message that the phone number is already registered
        return render_template("customers/sign_up.html")

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/sign/log_in', methods=['POST', 'GET'])
def log_in():
    if 'table' in session and session['table'] is not None:
        if request.method == 'POST':

            if 'customer' in session:
                session.pop('customer', None)

            user_phone = request.form['phone']

            print(user_phone)
            customer = Customer.get_by_phone(customer_phoneNumber=user_phone) #get_customer_by_phone(user_phone=user_phone) #not implemented yet
            if customer is not None:
                print('not non')
                session["customer"] = customer.to_dict()

                session.modified = True

                return redirect(url_for('customers.categories'))  #after making log in

        return render_template("customers/log_in.html")

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/categories')
def categories():
    if 'customer' in session and session['customer'] is not None:
        items_categories = MenuItems.get_categories()
        customer = Customer.from_dict(session['customer'])
        return render_template("customers/categories.html", items_categories=items_categories, user_name=customer.customer_name)

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('/categories/<category>')
def category_items(category):
    if 'customer' in session and session['customer'] is not None:
        menuItems = MenuItems.get_by_category(category)

        return render_template("customers/menuItems.html", category=category, menuItems=menuItems)

    else:
        return redirect(url_for('customers.home_page'))


@customers.route('categories/<category>/<menu_item>')
def dish_details(category, menu_item):
    if 'customer' in session and session['customer'] is not None:
        item = MenuItems.get(menu_item)
        return render_template("customers/item_details.html", category=category, menuItem = item)

    else:
         return redirect(url_for('customers.home_page'))
