import urllib.parse

from sqlalchemy import create_engine

from ProjectFiles.e_menu.utils.queries.customers import *
from ProjectFiles.e_menu.utils.queries.menuItems import *
from ProjectFiles.e_menu.utils.queries.tables import *
from ProjectFiles.e_menu.utils.queries.orders_details import *
from ProjectFiles.e_menu.utils.queries.orders import *
from ProjectFiles.e_menu.utils.queries.ratings import *
from ProjectFiles.e_menu.utils.queries.payment_methods import *

# Encode the password
encoded_password = urllib.parse.quote_plus('Mohammed@123')
# Construct the connection string
DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'

engine = create_engine(DATABASE, echo=True)


def generate_key(char) -> str:

    query_dict = {
        'C': GET_CUSTOMERS_TABLE,
        'M': GET_MENU_ITEMS_TABLE,
        'O': GET_ORDERS_REVERSE,
        'D': GET_ORDER_DETAILS_REVERSE
    }

    query = query_dict[char]

    conn = engine.connect()
    row = conn.execute(query).fetchone()
    conn.commit()
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

    prev_key = row[0]
    key_length = len(prev_key)
    number = int(prev_key[1:])

    next_number = number + 1
    next_number_length = len(str(next_number))
    n_zeros = (key_length - next_number_length - 1) * '0'
    string_next_number = char + n_zeros + str(next_number)
    print(string_next_number)
    return string_next_number
