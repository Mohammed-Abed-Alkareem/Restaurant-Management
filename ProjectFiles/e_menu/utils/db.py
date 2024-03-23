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
    # insert_menuItems_data()
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




def insert_table(data: list):
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()

    conn.execute(INSERT_INTO_TABLES, {'tableId': data[0], 'location': data[1], 'class': data[2], 'numOfSeats': data[3]})
    conn.commit()
    conn.close()


def insert_tables():
    tables_data = get_tables_data()
    print(tables_data)
    for table in tables_data:
        print(table)
        insert_table(table)


def insert_customers():
    customers_data = get_customers_data()
    for customer in customers_data:
        insert_customer(customer)

def insert_customer(data:list):
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()
    row = conn.execute(GET_CUSTOMERS_TABLE).fetchone()

    customer_id = generate_key(row, 'C')
    conn.execute(INSERT_CUSTOMERS_TABLE, {'customerId': customer_id, 'customer_name': data[0], 'customer_phoneNumber': data[1]})
    conn.commit()
    conn.close()


def get_menuItems_data(item_category):
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()
    rows = conn.execute(SELECT_MENU_ITEMS_BY_CATEGORY, {'item_category': item_category})
    return rows.fetchall()


def get_menuItems_categories():
    engine = create_engine(DATABASE, echo=True)
    conn = engine.connect()
    rows = conn.execute(GET_CATEGORIES_IN_MENU_ITEMS)

    category_list = [category[0] for category in rows.fetchall()]
    print(category_list)

    return category_list
