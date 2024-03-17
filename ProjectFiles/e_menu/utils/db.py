#this file contains the function for the database

from sqlalchemy import create_engine
import urllib.parse
from .queries.menuItems import *
from .queries.tables import *
from .queries.customers import *
from .read_initial_data import *

# Encode the password
encoded_password = urllib.parse.quote_plus('Mohammed@123')
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


def get_table_by_id(table_id):
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()
    try:
        table = conn.execute(SELECT_TABLE_BY_ID, {'tableId': int(table_id)}).fetchone()
        return table
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()


def insert_menuItems_data():
    menuItems_data = get_menuItems_data()
    for menuItem in menuItems_data:
        print(menuItem)


def insert_customers():
    customers_data = get_customers_data()
    for customer in customers_data:
        insert_customer(customer)

def insert_customer(data:list):
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()
    row = conn.execute(GET_CUSTOMERS_TABLE).fetchone()

    customer_id = generate_key(row, 'C')
    conn.execute(INSERT_CUSTOMERS_TABLE, {'customerId': customer_id, 'name': data[0], 'phoneNumber': data[1]})
    conn.commit()
    conn.close()