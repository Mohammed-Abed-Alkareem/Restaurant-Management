from . import *


class PaymentMethod:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @staticmethod
    def create_table():
        conn = engine.connect()
        try:
            conn.execute(CREATE_PAYMENT_METHODS_TABLE)
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def drop_table():
        conn = engine.connect()

        try:
            conn.execute(DROP_PAYMENT_METHODS_TABLE)
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_PAYMENT_METHODS_TABLE,
                         {'id': self.id, 'description': self.description})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        conn = engine.connect()
        try:
            payment_methods_objects = []
            payment_methods = conn.execute(SELECT_PAYMENT_METHODS_TABLE).fetchall()
            for payment_method in payment_methods:
                payment_methods_objects.append(cls(id=payment_method[0], description=payment_method[1]))
            return payment_methods_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
