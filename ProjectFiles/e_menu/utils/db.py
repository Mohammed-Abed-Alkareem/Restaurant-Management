#this file contains the function for the database

from .read_initial_data import *

from ProjectFiles.e_menu.customers.models.menuItems_model import *
from ProjectFiles.e_menu.customers.models.customers_model import *
from ProjectFiles.e_menu.customers.models.tables_model import *

# Encode the password
encoded_password = urllib.parse.quote_plus('mosatukba1')
# Construct the connection string
DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'


def init_db():
    # Create an engine
    engine = create_engine(DATABASE, echo=True)

    # Connect to the engine
    conn = engine.connect()

    #create all tables
    #______________________________
    conn.execute(CREATE_MENU_TABLE)
    conn.execute(CREATE_TABLES_TABLE)
    conn.execute(CREATE_CUSTOMERS_TABLE)

    # _________________________
    conn.commit()

    #inset any initial data
    # _________________________
    insert_menuItems_data()
    insert_tables()
    insert_customers()
    # _________________________
    conn.commit()

    conn.close()


def reset_db():
    engine = create_engine(DATABASE, echo=True)

    conn = engine.connect()

    #drop all tables
    # _________________________
    conn.execute(DROP_MENU_TABLE)
    conn.execute(DROP_TABLES_TABLE)
    conn.execute(DROP_CUSTOMERS_TABLE)
    # _________________________

    conn.commit()
    conn.close()
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
                menuItem["price"]
            )
            .insert())



