from . import *


class Customer:
    def __init__(self, *args):

        if len(args) == 2:
            self.customerId = generate_key()
            self.customer_name = args[0]
            self.customer_phoneNumber = args[1]

        else:
            self.customerId = args[0]
            self.customer_name = args[1]
            self.customer_phoneNumber = args[2]

    def insert(self):
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
        conn = engine.connect()

        try:
            customer = conn.execute(SELECT_CUSTOMER_BY_ID, {'customerId': customer_id}).fetchone()

            return cls(customer[0], customer[1], customer[2])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        conn = engine.connect()

        try:
            customers_objects = []
            customers = conn.execute(GET_CUSTOMERS_TABLE).fetchall()
            for customer in customers:
                customers_objects.append(cls(customer[0], customer[1],
                                             customer[2]))
            return customers_objects
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get_by_phone(cls, customer_phoneNumber):
        conn = engine.connect()

        try:
            customer = conn.execute(SELECT_CUSTOMER_BY_PHONE, {'customer_phoneNumber': customer_phoneNumber}).fetchone()

            return cls(customer[0], customer[1], customer[2])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    def to_dict(self):
        """Convert Customer object to a dictionary."""
        return {
            'customerId': self.customerId,
            'customer_name': self.customer_name,
            'customer_phoneNumber': self.customer_phoneNumber
        }

    @classmethod
    def from_dict(cls, data_dict):
        """Create a Customer object from a dictionary."""
        return cls(
            data_dict['customerId'],
            data_dict['customer_name'],
            data_dict['customer_phoneNumber']
        )

