from . import *


class Customer:
    def __init__(self, name, phone_number, id=generate_key('C')):
        self.id = id
        self.name = name
        self.phone_number = phone_number


    @staticmethod
    def create_table():
        conn = engine.connect()

        try:
            conn.execute(CREATE_CUSTOMERS_TABLE)
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @staticmethod
    def drop_table():
        conn = engine.connect()

        try:
            conn.execute(DROP_CUSTOMERS_TABLE)
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def insert(self):
        conn = engine.connect()

        try:
            conn.execute(INSERT_CUSTOMERS_TABLE,
                         {'id': self.id, 'name': self.name,
                          'phone_number': self.phone_number})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def delete(cls, id):
        conn = engine.connect()

        try:
            conn.execute(DELETE_FROM_CUSTOMERS, {'id': id})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def update(self, id, name, phone_number):
        pass

    @classmethod
    def get(cls, id):
        conn = engine.connect()

        try:
            customer = conn.execute(SELECT_CUSTOMER_BY_ID, {'id': id}).fetchone()
            return cls(id=customer[0], name=customer[1], phone_number=customer[2])
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
                customers_objects.append(cls(id=customer[0], name=customer[1], phone_number=customer[2]))
            return customers_objects
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get_by_phone(cls, phone_number):
        conn = engine.connect()

        try:
            customer = conn.execute(SELECT_CUSTOMER_BY_PHONE, {'phone_number': phone_number}).fetchone()
            return cls(id=customer[0], name=customer[1], phone_number=customer[2])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            data_dict['id'],
            data_dict['name'],
            data_dict['phone_number']
        )
