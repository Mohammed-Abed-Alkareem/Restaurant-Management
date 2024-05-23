from . import *


class Customer:
    def __init__(self, name, phone_number, id=None, gender=None, birth_year=None, favourite_cuisine=None):
        if id is None:
            id = generate_key('C')

        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.birth_year = birth_year
        self.favourite_cuisine = favourite_cuisine


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
                         {'id': self.id,
                          'name': self.name,
                          'phone_number': self.phone_number,
                          'gender': self.gender,
                          'birth_year': self.birth_year,
                          'favourite_cuisine': self.favourite_cuisine})
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
            return cls(id=customer[0], name=customer[1], phone_number=customer[2],
                       gender=customer[3], birth_year=customer[4], favourite_cuisine=customer[5])
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
                customers_objects.append(cls(id=customer[0], name=customer[1], phone_number=customer[2],
                                             gender=customer[3], birth_year=customer[4], favourite_cuisine=customer[5]))
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
            return cls(id=customer[0], name=customer[1], phone_number=customer[2],
                       gender=customer[3], birth_year=customer[4], favourite_cuisine=customer[5])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'gender': self.gender,
            'birth_year': self.birth_year,
            'favourite_cuisine': self.favourite_cuisine
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            id=data_dict['id'],
            name=data_dict['name'],
            phone_number=data_dict['phone_number'],
            gender=data_dict['gender'],
            birth_year=data_dict['birth_year'],
            favourite_cuisine=data_dict['favourite_cuisine']
        )
