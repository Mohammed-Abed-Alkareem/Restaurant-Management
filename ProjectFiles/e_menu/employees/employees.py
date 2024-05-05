import bcrypt
from flask import render_template, request, session, redirect, url_for, flash

from . import employees  # Import the blueprint from the package

from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from ProjectFiles.e_menu.models.payment_methods_model import *
from ProjectFiles.e_menu.models.orders_model import *
from ProjectFiles.e_menu.models.orders_details_model import *
from ProjectFiles.e_menu.models.ratings_model import *
from ProjectFiles.e_menu.models.empoyees_model import Employee

#allow only png images
ALLOWED_EXTENSIONS = {'png'}


@employees.route("/")
@employees.route("sign_in", methods=['GET', 'POST'])
def sign_in():
    session.clear()

    if request.method == 'GET':
        return render_template("employees/sign_in.html")
    else:
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        employee = Employee.get_by_phone_number(phone_number)
        if employee and bcrypt.checkpw(password.encode('utf-8'), employee['password']):
            session['employee_id'] = employee['id']
            session['employee_name'] = employee['name']
            session['employee_position'] = employee['position']
            return redirect(url_for('employees.sign_in'))
        else:
            flash("Invalid phone number or password", "danger")
            return redirect(url_for('employees.sign_in'))



@employees.route("dashboard")
def dashboard():
    # if 'employee_id' not in session:
    #     return redirect(url_for('employees.sign_in'))

    return render_template("employees/dashboard.html")


@employees.route("sign_out")
def sign_out():
    session.clear()
    return redirect(url_for('employees.sign_in'))


@employees.route("insert_employee", methods=['GET', 'POST'])
def insert_employee():
    if request.method == 'GET':
        return render_template("employees/insert_employee.html")
    else:
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        position = request.form.get('position')

        print(name, phone_number, password, position)

        # employee = Employee(name, phone_number, password, position)
        # if employee.insert():
        #     return "Employee added successfully"
        # else:
        #     return "Error adding employee"
        flash("Employee added successfully", "success")
        return redirect(url_for('employees.dashboard'))


@employees.route("delete_employee/<employee_id>")
def delete_employee(employee_id):
    Employee.delete(employee_id)
    return "Employee deleted successfully"

@employees.route("view_employees")
def view_employees():
    employees = Employee.get_all()
    return render_template("employees/view_employees.html", employees=employees)


@employees.route("change_availability/<item_id>")
def change_availability(item_id):

    MenuItems.change_availability(item_id)
    flash("Item availability changed successfully", "success")
    return redirect(url_for('employees.view_menu_items'))


@employees.route("add_table", methods=['GET', 'POST'])
def add_table():
    if request.method == 'GET':
        return

    table_code = request.form.get('table_code')
    table_location = request.form.get('table_location')
    table_type = request.form.get('table_type')
    table_seats = request.form.get('table_seats')

    table = Table(table_location, table_type, table_seats)
    if table.insert():
        return "Table added successfully"
    else:
        return "Error adding table"



#update menu item
@employees.route("update_menu_item/<item_id>", methods=['GET', 'POST'])
def update_menu_item(item_id):
    if request.method == 'GET':
        item = MenuItems.get(item_id)
        return render_template("employees/update_menu_item.html", item=item)
    else:
        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        item_description = request.form.get('item_description')
        item_category = request.form.get('item_category')
        item_is_available = request.form.get('item_is_available')
        if MenuItems.update(item_id, item_name, item_price, item_description, item_category, item_is_available):
            return "Item updated successfully"
        else:
            return "Error updating item"




@employees.route("add_menu_item", methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'GET':
        return render_template("employees/add_menu_item.html")
    else:

        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        item_description = request.form.get('item_description')
        item_category = request.form.get('item_category')
        item_is_available = True
        item = MenuItems(item_name, item_price, item_description, item_category, item_is_available)

        uploaded_file = request.files['item_image']
        file_path = f"ProjectFiles/e_menu/static/img/menuItems/{item.id}.png"

        #check if saved successfully



        if item.insert():
            uploaded_file.save(file_path)
            return "Item added successfully"


@employees.route("view_menu_items")
def view_menu_items():
    items = MenuItems.get_all()
    if items:
        for item in items:
            print(item.is_available)
    return render_template("employees/view_menu_items.html", menuItems=items)