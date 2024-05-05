from flask import render_template, request

from . import employees  # Import the blueprint from the package

from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from ProjectFiles.e_menu.models.payment_methods_model import *
from ProjectFiles.e_menu.models.orders_model import *
from ProjectFiles.e_menu.models.orders_details_model import *
from ProjectFiles.e_menu.models.ratings_model import *

#allow only png images
ALLOWED_EXTENSIONS = {'png'}


@employees.route("/")
def home_page():
    return render_template ("managers/home_page.html")



@employees.route("change_availibility/<item_id>", methods=['POST'])
def change_availability(item_id):

    is_available = request.form.get('is_available')
    MenuItems.change_availability(item_id, is_available)
    return "Item availability changed successfully"


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
        return render_template("managers/update_menu_item.html", item=item)
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
        return render_template("managers/add_menu_item.html")
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

