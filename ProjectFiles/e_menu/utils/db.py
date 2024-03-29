
from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from .read_initial_data import *


def init_db():

    # create all tables
    # ______________________________
    MenuItems.create_table()
    Table.create_table()
    Customer.create_table()
    # _________________________

    # inset any initial data
    # _________________________
    insert_menuItems_data()
    insert_tables()
    insert_customers()
    # _________________________


def reset_db():

    # drop all tables
    # _________________________
    MenuItems.drop_table()
    Table.drop_table()
    Customer.drop_table()
    # _________________________

    init_db()


def insert_tables():
    tables_data = get_tables_data()

    for table in tables_data:
        (Table
             (
             table["tableId"],
             table["location"],
             table["class"],
             table["numOfSeats"]
         )
         .insert())


def insert_customers():
    customers_data = get_customers_data()
    for customer in customers_data:
        Customer.insert(Customer(customer[0], customer[1]))


def insert_menuItems_data():
    menuItems_data = get_menuItems_data()
    print(menuItems_data)
    for menuItem in menuItems_data:
        (MenuItems

            (
                menuItem["id"], menuItem["name"],
                menuItem["description"], menuItem["category"],
                menuItem["price"], True
            )
            .insert())




