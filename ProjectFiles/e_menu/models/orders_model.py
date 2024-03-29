from . import *


class Order:
    def __init__(self, id, customer_id, table_code, payment_id, order_date):
        self.id = id
        self.customer_id = customer_id
        self.table_code = table_code
        self.payment_id = payment_id
        self.order_date = order_date

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_ORDERS_TABLE,
                         {'id': self.id, 'customer_id': self.customer_id, 'table_code': self.table_code,
                          'payment_id': self.payment_id, 'order_date': self.order_date})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get_customer_current_order(cls, customer_id):
        conn = engine.connect()
        try:
            order = conn.execute(GET_CUSTOMER_CURRENT_ORDER, {'customer_id': customer_id}).fetchone()
            return cls(id=order[0], customer_id=order[1],
                       table_code=order[2], payment_id=order[3],
                       order_date=order[4])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        conn = engine.connect()
        try:
            orders_objects = []
            orders = conn.execute(GET_ORDERS_TABLE).fetchall()
            for order in orders:
                orders_objects.append(cls(id=order[0], customer_id=order[1],
                                          table_code=order[2], payment_id=order[3],
                                          order_date=order[4]))
            return orders_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_table_current_order(cls, table_code):
        conn = engine.connect()
        try:
            order = conn.execute(GET_TABLE_CURRENT_ORDER, {'table_code': table_code}).fetchone()
            return cls(id=order[0], customer_id=order[1],
                       table_code=order[2], payment_id=order[3],
                       order_date=order[4])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
