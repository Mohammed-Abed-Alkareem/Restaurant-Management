import pandas as pd


PATH = 'utils/csvFiles/'

def get_menu_items_data():
    df = pd.read_csv(PATH + 'menuItems.csv')
    df.fillna('', inplace=True)

    menuItems_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'name': row['name'],
            'description': row['description'],
            'category': row['category'],
            'price': row['price']
        }

        menuItems_data.append(data)

    return menuItems_data


def get_tables_data():
    df = pd.read_csv(PATH + 'tables.csv')
    df.fillna('', inplace=True)

    tables_data = []

    for index, row in df.iterrows():
        data = {
            'code': row['code'],
            'seats': row['seats'],
            'location': row['location'],
            'type': row['type']
        }

        tables_data.append(data)

    return tables_data


def get_payment_methods_data():
    df = pd.read_csv(PATH + 'paymentMethods.csv')

    df.fillna('', inplace=True)

    payment_methods_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'description': row['description']
        }

        payment_methods_data.append(data)

    return payment_methods_data


def get_customers_data():
    df = pd.read_csv(PATH + 'customers.csv')
    df.fillna('', inplace=True)

    customers_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'name': row['name'],
            'phone_number': row['phone_number']
        }

        customers_data.append(data)

    return customers_data


def get_orders_data():
    df = pd.read_csv(PATH + 'orders.csv')
    df.fillna('', inplace=True)

    orders_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'customer_id': row['customer_id'],
            'table_code': row['table_code'],
            'payment_method_id': row['payment_method_id'],
            'order_date': row['order_date']
        }

        orders_data.append(data)

    return orders_data


def get_orders_details_data():
    df = pd.read_csv(PATH + 'orderDetails.csv')
    df.fillna('', inplace=True)

    orders_details_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'order_id': row['order_id'],
            'item_id': row['item_id'],
            'price': row['price'],
            'quantity': row['quantity']
        }

        orders_details_data.append(data)

    return orders_details_data


def get_ratings_data():
    df = pd.read_csv(PATH + 'ratings.csv')
    df.fillna('', inplace=True)

    ratings_data = []

    for index, row in df.iterrows():
        data = {
            'id': row['id'],
            'order_id': row['order_id'],
            'rating': row['rating'],
            'food_rating': row['food_rating'],
            'service_rating': row['service_rating']
        }

        ratings_data.append(data)

    return ratings_data
