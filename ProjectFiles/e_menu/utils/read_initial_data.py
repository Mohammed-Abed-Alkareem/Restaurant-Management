import pandas as pd
from faker import Faker
import random
import time


def get_menuItems_data():
    df = pd.read_csv('utils\\csvFiles\\menuItems.csv')
    menuItems_data = []
    for index, row in df.iterrows():
        data = (f"({row['itemId']},{row['name']},{row['description']},{row['category']},{row['price']})")
        menuItems_data.append(data)

    return menuItems_data


def generate_key(row, char: str) -> str:
    print(row)
    if row is None:
        if char == 'C':
            return 'C0001'
        elif char == 'F':
            return 'F001'

    prev_key = row[0]
    key_length = len(prev_key)
    number = int(prev_key[1:])

    next_number = number + 1
    next_number_length = len(str(next_number))
    n_zeros = (key_length - next_number_length - 1) * '0'
    string_next_number = char + n_zeros + str(next_number)
    print(string_next_number)
    return string_next_number


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

