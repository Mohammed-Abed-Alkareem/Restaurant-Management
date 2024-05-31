from datetime import datetime, timedelta

import pandas as pd
from faker import Faker
import random
import time

fake = Faker()


def gen_datetime(min_year, max_year):
    # Generate a datetime in the format yyyy-mm-dd hh:mm:ss
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    hour = random.randint(6, 21)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return datetime(year, month, day, hour, minutes, seconds)


def read_data_from_csv():
    customers = pd.read_csv('csvFiles/customers.csv')
    tables = pd.read_csv('csvFiles/tables.csv')
    payment_methods = pd.read_csv('csvFiles/paymentMethods.csv')
    menu_items = pd.read_csv('csvFiles/menuItems.csv')

    return customers, tables, payment_methods, menu_items


def generate_key(char, data) -> str:
    if len(data) == 0:
        if char == 'C':
            return 'C0001'
        elif char == 'M':
            return 'M001'
        elif char == 'O':
            return 'O00001'
        elif char == 'D':
            return 'D000001'
        elif char == 'R':
            return 'R00001'

    prev_key = data[-1]['id']
    key_length = len(prev_key)
    number = int(prev_key[1:])

    next_number = number + 1
    next_number_length = len(str(next_number))
    n_zeros = (key_length - next_number_length - 1) * '0'
    string_next_number = char + n_zeros + str(next_number)
    return string_next_number


def generate_customers():
    random.seed(time.time())  # Seed the random number generator with current date and time

    # Generate a list of elements with format ({name},{phone number})
    genders = ['Male', 'Female']
    cuisines = ['Turkish', 'Mediterranean', 'American', 'Italian', 'French', 'Greek', 'Seafood', 'Beverages']

    customers_data = []

    for _ in range(50):

        prefixes = ['052', '056', '059']
        prefix = random.choice(prefixes)
        suffix = fake.numerify('#######')  # Generates a 7-digit random number

        fake_phone_number = f"{prefix}{suffix}"
        fake_gender = random.choice(genders)
        fake_birth_year = random.randint(1950, 2010)  # Random birth year between 1950 and 2010
        fake_favourite_cuisine = random.choice(cuisines)

        if fake_gender == 'Male':
            fake_name = fake.first_name_male() + ' ' + fake.last_name()
        else:
            fake_name = fake.first_name_female() + ' ' + fake.last_name()
        customers_data.append({
            'id': generate_key('C', customers_data),
            'name': fake_name,
            'phone_number': fake_phone_number,
            'gender': fake_gender,
            'birth_year': fake_birth_year,
            'favourite_cuisine': fake_favourite_cuisine
        })

    customers_df = pd.DataFrame(customers_data)

    customers_df.to_csv('csvFiles/customers.csv', index=False)


def generate_orders(customers, tables, payment_methods, min_orders=1, max_orders=5):
    orders_data = []
    for customer_id in customers['id']:
        num_orders = fake.random_int(min=min_orders, max=max_orders)
        for i in range(num_orders):
            orders_data.append({
                'id': generate_key('O', orders_data),
                'customer_id': customer_id,
                'table_code': fake.random_element(tables['code'].tolist()),
                'payment_method_id': fake.random_element(payment_methods['id'].tolist()),
                'order_date': gen_datetime(min_year=2020, max_year=2025)
            })

    orders_df = pd.DataFrame(orders_data)
    orders_df.to_csv('csvFiles/orders.csv', index=False)


def generate_order_details(orders, menu_items):
    order_details_data = []
    for order_id in orders['id']:
        # Example meal combination: 1 appetizer, 1 main course, 1 drink, 1 dessert
        categories = ['MAZE & APPETIZERS TO SHARE', 'CHICKEN', 'SOFT DRINK', 'DESSERT']
        selected_items = menu_items[menu_items['category'].isin(categories)].groupby('category').sample(n=1)

        for _, item in selected_items.iterrows():
            order_details_data.append({
                'id': generate_key('D', order_details_data),
                'order_id': order_id,
                'item_id': item['id'],
                'price': item['price'],
                'quantity': fake.random_int(min=1, max=3)
            })

    order_details_df = pd.DataFrame(order_details_data)
    order_details_df.to_csv('csvFiles/orderDetails.csv', index=False)


def generate_ratings(orders):
    ratings_data = []
    for index, order in orders.iterrows():
        ratings_data.append({
            'id': generate_key('R', ratings_data),
            'order_id': order['id'],
            'rating': fake.random_int(min=1, max=5),
            'food_rating': fake.random_int(min=1, max=5),
            'service_rating': fake.random_int(min=1, max=5)
        })

    ratings_df = pd.DataFrame(ratings_data)
    ratings_df.to_csv('csvFiles/ratings.csv', index=False)


if __name__ == '__main__':
    generate_customers()
    customers, tables, payment_methods, menu_items = read_data_from_csv()

    generate_orders(customers, tables, payment_methods)

    orders = pd.read_csv('csvFiles/orders.csv')

    generate_order_details(orders, menu_items)

    generate_ratings(orders)
