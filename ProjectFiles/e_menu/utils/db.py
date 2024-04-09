
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
    encoded_password = urllib.parse.quote_plus('mosatukba1')
    # Construct the connection string
    DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'
    db_path = DATABASE  # Change to your actual database path
    main(db_path)

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
             table["code"],
             table["location"],
             table["type"],
             table["seats"]
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


fake = Faker()


def connect_db(db_path):
    """Connect to the SQL database."""
    return sqlite3.connect(db_path)


def fetch_data(conn):
    """Fetch necessary existing data from the database."""
    customer_ids = pd.read_sql_query("SELECT id FROM customers", conn)
    table_codes = pd.read_sql_query("SELECT code FROM tables", conn)
    payment_ids = pd.read_sql_query("SELECT id FROM paymentMethods", conn)
    menu_items = pd.read_sql_query("SELECT id, category, price FROM menuItems", conn)
    return customer_ids, table_codes, payment_ids, menu_items


def generate_orders(customer_ids, table_codes, payment_ids, min_orders=1, max_orders=5):
    """Ensure each customer has at least one order and optionally more."""
    orders_data = []
    for customer_id in customer_ids['id']:
        num_orders = fake.random_int(min=min_orders, max=max_orders)
        for _ in range(num_orders):
            orders_data.append({
                'customer_id': customer_id,
                'table_code': fake.random_element(table_codes['code'].tolist()),
                'payment_id': fake.random_element(payment_ids['id'].tolist()),
                'order_date': fake.date_time_this_year()
            })
    return orders_data


def generate_order_details(order_ids, menu_items):
    """Generate order details with realistic meal combinations."""
    order_details_data = []
    for order_id in order_ids['id']:
        # Example meal combination: 1 appetizer, 1 main course, 1 drink, 1 dessert
        categories = ['MAZE & APPETIZERS TO SHARE', 'CHICKEN', 'SOFT DRINK', 'DESSERT']
        selected_items = menu_items[menu_items['category'].isin(categories)].groupby('category').sample(n=1)

        for _, item in selected_items.iterrows():
            order_details_data.append({
                'order_id': order_id,
                'item_id': item['id'],
                'price': item['price'],
                'quantity': fake.random_int(min=1, max=3)
            })
    return order_details_data


def main(db_path):
    conn = connect_db(db_path)
    customer_ids, table_codes, payment_ids, menu_items = fetch_data(conn)

    orders_data = generate_orders(customer_ids, table_codes, payment_ids)
    pd.DataFrame(orders_data).to_sql('Orders', conn, if_exists='append', index=False)

    order_ids = pd.read_sql_query("SELECT id FROM Orders", conn)
    order_details_data = generate_order_details(order_ids, menu_items)
    pd.DataFrame(order_details_data).to_sql('OrderDetails', conn, if_exists='append', index=False)

    conn.close()







