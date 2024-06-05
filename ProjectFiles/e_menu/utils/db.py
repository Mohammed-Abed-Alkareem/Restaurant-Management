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
    insert_employees()
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
                 code=table["code"],
                 location=table["location"],
                 type=table["type"],
                 seats=table["seats"]
            )
         .insert())


def insert_customers():
    customers_data = get_customers_data()
    for customer in customers_data:
        customer_object = Customer(
            id=customer['id'],
            name=customer['name'],
            phone_number=customer['phone_number'],
            gender=customer['gender'],
            birth_year=customer['birth_year'],
            favourite_cuisine=customer['favourite_cuisine']
        )
        customer_object.insert()


def insert_payment_methods():
    payment_methods_data = get_payment_methods_data()

    for payment_method in payment_methods_data:
        payment_method_object = PaymentMethod(
            id=payment_method['id'],
            description=payment_method['description']
        )
        payment_method_object.insert()


def insert_menuItems_data():
    menuItems_data = get_menu_items_data()
    for menuItem in menuItems_data:
        (MenuItems
            (
             id=menuItem["id"],
             name=menuItem["name"],
             description=menuItem["description"],
             category=menuItem["category"],
             price=menuItem["price"],
             cuisine_type=menuItem["cuisine_type"]
            )
         .insert())


def insert_orders():
    orders_data = get_orders_data()

    for order in orders_data:
        order_object = Order(
            id=order['id'],
            customer_id=order['customer_id'],
            table_code=order['table_code'],
            payment_method_id=order['payment_method_id'],
            order_date=order['order_date']

        )

        order_object.insert()


def insert_orders_details():
    orders_details_data = get_orders_details_data()

    for order_details in orders_details_data:
        order_details_object = OrderDetails(
            id=order_details['id'],
            order_id=order_details['order_id'],
            item_id=order_details['item_id'],
            price=order_details['price'],
            quantity=order_details['quantity']
        )

        order_details_object.insert()


def insert_ratings():
    ratings_data = get_ratings_data()

    for rating in ratings_data:
        rating_object = Rating(
            id=rating['id'],
            order_id=rating['order_id'],
            rating=rating['rating'],
            food_rating=rating['food_rating'],
            service_rating=rating['service_rating']
        )

        rating_object.insert()


def insert_employees():
    employees_data = get_employees_data()

    for employee in employees_data:
        employee_object = Employee(
            name=employee['name'],
            phone_number=employee['phone_number'],
            salary=employee['salary'],
            position=employee['position'],
            password=employee['password']
        )

        employee_object.insert()
