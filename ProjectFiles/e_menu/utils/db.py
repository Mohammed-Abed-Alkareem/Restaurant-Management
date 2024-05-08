from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from ProjectFiles.e_menu.models.payment_methods_model import *
from ProjectFiles.e_menu.models.orders_model import *
from ProjectFiles.e_menu.models.orders_details_model import *
from ProjectFiles.e_menu.models.ratings_model import *
from ProjectFiles.e_menu.models.employees_model import *


from ProjectFiles.e_menu.utils.read_initial_data import *


def init_db():
    # create all tables
    # ______________________________
    MenuItems.create_table()
    Table.create_table()
    Customer.create_table()
    PaymentMethod.create_table()
    Order.create_table()
    OrderDetails.create_table()
    Rating.create_table()
    Employee.create_table()
    # _________________________

    # inset any initial data
    # _________________________
    insert_menuItems_data()
    insert_tables()
    insert_customers()
    insert_payment_methods()
    insert_orders()
    insert_orders_details()
    insert_ratings()
    # insert_employee()
    # _________________________


def reset_db():
    # drop all tables
    # _________________________

    OrderDetails.drop_table()
    Rating.drop_table()
    Order.drop_table()
    MenuItems.drop_table()
    Table.drop_table()
    Customer.drop_table()
    PaymentMethod.drop_table()
    Employee.drop_table()
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
        customer_object = Customer(
            customer['id'],
            customer['name'],
            customer['phone_number']
        )
        customer_object.insert()


def insert_payment_methods():
    payment_methods_data = get_payment_methods_data()

    for payment_method in payment_methods_data:
        payment_method_object = PaymentMethod(
            payment_method['id'],
            payment_method['description']
        )
        payment_method_object.insert()


def insert_menuItems_data():
    menuItems_data = get_menu_items_data()
    for menuItem in menuItems_data:
        (MenuItems

             (
             menuItem["id"], menuItem["name"],
             menuItem["description"], menuItem["category"],
             menuItem["price"], True
         )
         .insert())


def insert_orders():
    orders_data = get_orders_data()

    for order in orders_data:
        order_object = Order(
            order['id'],
            order['customer_id'],
            order['table_code'],
            order['payment_method_id'],
            order['order_date']

        )

        order_object.insert()


def insert_orders_details():
    orders_details_data = get_orders_details_data()

    for order_details in orders_details_data:
        order_details_object = OrderDetails(
            order_details['id'],
            order_details['order_id'],
            order_details['item_id'],
            order_details['price'],
            order_details['quantity']

        )

        order_details_object.insert()


def insert_ratings():
    ratings_data = get_ratings_data()

    for rating in ratings_data:
        rating_object = Rating(
            rating['id'],
            rating['order_id'],
            rating['rating'],
            rating['food_rating'],
            rating['service_rating']
        )

        rating_object.insert()

if __name__ == '__main__':
    reset_db()