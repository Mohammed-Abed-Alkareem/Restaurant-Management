import urllib.parse
import random
from sqlalchemy import create_engine

from ProjectFiles.e_menu.utils.queries.customers import *
from ProjectFiles.e_menu.utils.queries.menuItems import *
from ProjectFiles.e_menu.utils.queries.tables import *
from ProjectFiles.e_menu.utils.queries.orders_details import *
from ProjectFiles.e_menu.utils.queries.orders import *
from ProjectFiles.e_menu.utils.queries.ratings import *
from ProjectFiles.e_menu.utils.queries.payment_methods import *
from ProjectFiles.e_menu.utils.queries.employees import *
from ProjectFiles.e_menu.utils.queries.employees import *

# Encode the password
encoded_password = urllib.parse.quote_plus('Mohammed@123')
print(encoded_password)
# Construct the connection string
DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'

try:
    engine = create_engine(DATABASE, echo=True)
    print("Connection successful")

except Exception as e:
    print(f"Error: {e}")
    exit(1)


def generate_key(char):
    conn = engine.connect()
    if char != 'T':
        query_dict = {
            'C': GET_CUSTOMERS_TABLE,
            'M': GET_MENU_ITEMS_TABLE,
            'O': GET_ORDERS_REVERSE,
            'D': GET_ORDER_DETAILS_REVERSE,
            'R': GET_RATINGS_TABLE_REVERSED,
            'E': GET_EMPLOYEES_TABLE_REVERSED
        }

        query = query_dict[char]

        row = conn.execute(query).fetchone()

        conn.close()

        if row is None:
            if char == 'C':
                return 'C0001'
            elif char == 'M':
                return 'M001'
            elif char == 'O':
                return 'O00001'
            elif char == 'D':
                return 'D00001'
            elif char == 'R':
                return 'R00001'
            elif char == 'E':
                return 'E001'

        prev_key = row[0]
        key_length = len(prev_key)
        number = int(prev_key[1:])

        next_number = number + 1
        next_number_length = len(str(next_number))
        n_zeros = (key_length - next_number_length - 1) * '0'
        string_next_number = char + n_zeros + str(next_number)
        print(string_next_number)
        return string_next_number
    else:
        while True:
            new_table_code = random.randint(100000, 999999)
            tables = conn.execute(SELECT_TABLES).fetchall()
            conn.close()
            existing_table_codes = [table.code for table in tables]
            if new_table_code not in existing_table_codes:
                return new_table_code
