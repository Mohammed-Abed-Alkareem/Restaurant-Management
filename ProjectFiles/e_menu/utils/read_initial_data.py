import random
import time
import pandas as pd
from faker import Faker


def get_menuItems_data():
    df = pd.read_csv('utils\\csvFiles\\menuItems.csv')
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
    df = pd.read_csv('utils\\csvFiles\\tables.csv')
    df.fillna('', inplace=True)

    tables_data = []

    for index, row in df.iterrows():
        data = {
            'tableId': row['tableId'],
            'numOfSeats': row['numOfSeats'],
            'location': row['location'],
            'class': row['class']
        }

        tables_data.append(data)

    return tables_data


def get_customers_data():
    random.seed(time.time())  # Seed the random number generator with current date and time

    fake = Faker()  # Create a Faker instance

    # Generate a list of elements with format ({name},{phone number})
    customers_data = []
    for _ in range(50):
        fake_name = fake.name()

        prefixes = ['052', '056', '059']
        prefix = random.choice(prefixes)
        suffix = fake.numerify('#######')  # Generates a 7-digit random number

        fake_phone_number = f"{prefix}{suffix}"

        customers_data.append([fake_name, fake_phone_number])

    return customers_data
