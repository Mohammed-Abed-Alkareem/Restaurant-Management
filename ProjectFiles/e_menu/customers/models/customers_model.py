from sqlalchemy import create_engine
import urllib.parse
from ProjectFiles.e_menu.utils.queries.customers import *

# Encode the password
encoded_password = urllib.parse.quote_plus('Mohammed@123')
# Construct the connection string
DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'


class Customer:
    def __init__(self, customerId, customer_name, customer_phoneNumber):
        self.customerId = customerId
        self.customer_name = customer_name
        self.customer_phoneNumber = customer_phoneNumber

    def insert(self):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()

        try:
            conn.execute(INSERT_CUSTOMERS_TABLE,
                         {'customerId': self.customerId, 'customer_name': self.customer_name,
                          'customer_phoneNumber': self.customer_phoneNumber})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def delete(cls, customer_id):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()

        try:
            conn.execute(INSERT_CUSTOMERS_TABLE,
                         {'customerId': customer_id})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def update(self, customer_id, name, phone_number):
        pass

    @classmethod
    def get(cls, customer_id):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()

        try:
            customer = conn.execute(SELECT_CUSTOMER_BY_ID, {'customerId': customer_id}).fetchone()

            return cls(customerId=customer[0], customer_name=customer[1], customer_phoneNumber=customer[2])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()


        try:
            customers_objects = []
            customers = conn.execute(GET_CUSTOMERS_TABLE).fetchall()
            for customer in customers:
                customers_objects.append(cls(customerId=customer[0], customer_name=customer[1],
                                             customer_phoneNumber=customer[2]))
            return customers_objects
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()



