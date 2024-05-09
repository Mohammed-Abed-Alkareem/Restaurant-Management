import bcrypt
import os
from flask import render_template, request, session, redirect, url_for, flash, current_app

from . import employees  # Import the blueprint from the package

from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from ProjectFiles.e_menu.models.payment_methods_model import *
from ProjectFiles.e_menu.models.orders_model import *
from ProjectFiles.e_menu.models.orders_details_model import *
from ProjectFiles.e_menu.models.ratings_model import *
from ProjectFiles.e_menu.models.employees_model import Employee

#allow only png images
ALLOWED_EXTENSIONS = {'png'}




@employees.route("sign_out")
def sign_out():
    session.clear()
    return redirect(url_for('employees.sign_in'))





@employees.route("delete_employee/<employee_id>")
def delete_employee(employee_id):
    Employee.delete(employee_id)
    return "Employee deleted successfully"



#update menu item
@employees.route("update_menu_item/<item_id>", methods=['GET', 'POST'])
def update_menu_item(item_id):

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))



    if request.method == 'GET':
        item = MenuItems.get(item_id)
        return render_template("employees/update_menu_item.html", menuItem=item)
    else:

        item = MenuItems.get(item_id)

        print(item.id
              , item.name
              , item.description
              )

        item_name = request.form.get('name')
        item_price = request.form.get('price')
        item_description = request.form.get('description')

        uploaded_file = request.files['image']
        if uploaded_file:
            file_path = os.path.join(current_app.root_path, "static", "img", "menuItems", f"{item_id}.png")
            uploaded_file.save(file_path)

        if item.update(name=item_name, description=item_description, price=item_price):
            flash("Item updated successfully", "success")
            return redirect(url_for('employees.view_menu_items'))


        else:
            flash("Error updating item", "danger")
            return redirect(url_for('employees.update_menu_item', item_id=item_id))







@employees.route("update_employee/<employee_id>", methods=['GET', 'POST'])
def update_employee(employee_id):

        if 'employee_id' not in session:
            return redirect(url_for('employees.sign_in'))

        employee = Employee.get(employee_id)
        if request.method == 'GET':

            return render_template("employees/update_employee.html", employee=employee)
        else:
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            salary = request.form.get('salary')
            position = request.form.get('position')
            if employee.update(name=name, phone_number=phone_number, salary=salary, position=position):
                return "Employee updated successfully"
            else:
                return "Error updating employee"




#______________________________________________
#|
#|          Done
#______________________________________________
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
        if employee:
            # Here, you should use the hashed password stored in the employee object
            hashed_password = employee.password
            print(employee.password)
            print(password)

            if  bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                print("Password is correct")
                session['employee_id'] = employee.id
                session['employee_name'] = employee.name
                session['employee_position'] = employee.position
                return redirect(url_for('employees.dashboard'))
            else:
                print("Password is incorrect")


        flash("Invalid phone number or password", "danger")
        return redirect(url_for('employees.sign_in'))

@employees.route("dashboard")
def dashboard():
    # if 'employee_id' not in session:
    #     return redirect(url_for('employees.sign_in'))

    print(session)
    return render_template("employees/dashboard.html")


@employees.route("change_availability/<item_id>")
def change_availability(item_id):

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    MenuItems.change_availability(item_id)
    flash("Item availability changed successfully", "success")
    return redirect(url_for('employees.view_menu_items'))


@employees.route("add_menu_item", methods=['GET', 'POST'])
def add_menu_item():

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    if request.method == 'GET':
        categories = MenuItems.get_categories()

        return render_template("employees/add_menu_item.html", categories=categories)
    else:

        item_name = request.form.get('item_name')
        item_price = request.form.get('item_price')
        item_description = request.form.get('item_description')
        item_category = request.form.get('item_category')

        item = MenuItems(name=item_name, description=item_description, category=item_category, price=item_price)

        uploaded_file = request.files['item_image']
        if uploaded_file:
            file_path = os.path.join(current_app.root_path, "static", "img", "menuItems", f"{item.id}.png")
            uploaded_file.save(file_path)

        if item.insert():

            flash("Item added successfully", "success")
        else:
            flash("Error adding item", "danger")

        return redirect(url_for('employees.dashboard'))


@employees.route("view_menu_items")
def view_menu_items():

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    items = MenuItems.get_all()
    return render_template("employees/view_menu_items.html", menuItems=items)


@employees.route("delete_menu_item/<item_id>") # this will be in the view menu items page
def delete_menu_item(item_id):

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    if MenuItems.delete(item_id):
        #delete the image of the item
        file_path = os.path.join(current_app.root_path, "static", "img", "menuItems", f"{item_id}.png")
        if os.path.exists(file_path):
            os.remove(file_path)

        flash("Item deleted successfully", "success")
        return redirect(url_for('employees.view_menu_items'))
    else:
        flash("Error deleting item", "danger")
        return redirect(url_for('employees.view_menu_items'))


@employees.route("view_tables")
def view_tables():

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    tables = Table.get_all()
    return render_template("employees/view_tables.html", tables=tables)


@employees.route("update_table/<table_code>", methods=['GET', 'POST'])
def update_table(table_code):

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))
    table = Table.get(table_code)
    if request.method == 'GET':

        return render_template("employees/update_table.html", table=table)
    else:
        table_location = request.form.get('table_location')
        table_type = request.form.get('table_type')
        table_seats = request.form.get('table_seats')
        if table.update(location=table_location, type=table_type, seats=table_seats):
            flash("Table updated successfully", "success")
            return redirect(url_for('employees.view_tables'))
        else:
            flash("Error updating table", "danger")
            return redirect(url_for('employees.view_tables'))

@employees.route("delete_table/<table_code>")
def delete_table(table_code):

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    if Table.delete(table_code):
        flash("Table deleted successfully", "success")
        return redirect(url_for('employees.view_tables'))
    else:
        flash("Error deleting table", "danger")
        return redirect(url_for('employees.view_tables'))

@employees.route("insert_employee", methods=['GET', 'POST'])
def insert_employee():

    # if 'employee_id' not in session:
    #     return redirect(url_for('employees.sign_in'))

    if request.method == 'GET':
        return render_template("employees/insert_employee.html")
    else:
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        position = request.form.get('position')
        salary = request.form.get('salary')
        print(name, phone_number, salary, password, position)

        employee = Employee(name=name, phone_number=phone_number, salary=salary, position=position, password=password)
        print(employee.id, employee.name, employee.phone_number, employee.salary, employee.password,
              employee.position)
        if employee.insert():
            flash("Employee added successfully", "success")
        else:
            flash("Error adding employee", "danger")

        return redirect(url_for('employees.dashboard'))


@employees.route("add_table", methods=['GET', 'POST'])
def add_table():

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    if request.method == 'GET':
        return render_template("employees/add_table.html")

    table_location = request.form.get('table_location')
    table_type = request.form.get('table_type')
    table_seats = request.form.get('table_seats')

    table = Table(location=table_location, type=table_type, seats=table_seats)
    if table.insert():
        flash("Table added successfully", "success")
        return redirect(url_for('employees.view_tables'))
    else:
        flash("Error adding table", "danger")
        return redirect(url_for('employees.add_table'))

@employees.route("view_employees")
def view_employees():

    if 'employee_id' not in session:
        return redirect(url_for('employees.sign_in'))

    employees = Employee.get_all()
    return render_template("employees/view_employees.html", employees=employees)

