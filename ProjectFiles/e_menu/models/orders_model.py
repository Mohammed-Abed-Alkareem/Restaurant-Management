from datetime import datetime

from . import *


class Order:
    def __init__(self, customer_id, table_code, payment_method_id, id=None, order_date=None):
        if id is None:
            id = generate_key('O')

        if order_date is None:
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.id = id
        self.customer_id = customer_id
        self.table_code = table_code
        self.payment_method_id = payment_method_id
        #current date
        self.order_date = order_date
    # def __init__(self, *args):
    #     if len(args) == 3:
    #         self.id = generate_key('O')
    #         self.customer_id = args[0]
    #         self.table_code = args[1]
    #         self.payment_method_id = args[2]
    #         self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     else:
    #         self.id = args[0]
    #         self.customer_id = args[1]
    #         self.table_code = args[2]
    #         self.payment_method_id = args[3]
    #         self.order_date = args[4]


    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_ORDERS_TABLE,
                         {'id': self.id, 'customer_id': self.customer_id, 'table_code': self.table_code,
                          'payment_method_id': self.payment_method_id, 'order_date': self.order_date})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()


    @staticmethod
    def create_table():
        conn = engine.connect()

        try:
            conn.execute(CREATE_ORDERS_TABLE)
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
            conn.execute(DROP_ORDERS_TABLE)
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
                       table_code=order[2], payment_method_id=order[3],
                       order_date=order[4])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls, table_code=None, customer_id=None, payment_method_id=None, from_date=None, to_date=None):
        conn = engine.connect()
        try:
            orders_objects = []

            # Base query
            query = "SELECT * FROM orders WHERE 1=1"

            # Parameters dictionary
            params = {}

            # Append conditions to the query
            if customer_id is not None:
                query += " AND customer_id = :customer_id"
                params['customer_id'] = customer_id
            if table_code is not None:
                query += " AND table_code = :table_code"
                params['table_code'] = table_code
            if payment_method_id is not None:
                query += " AND payment_method_id = :payment_method_id"
                params['payment_method_id'] = payment_method_id
            if from_date is not None:
                if to_date is None:
                    to_date = datetime.now().strftime("%Y-%m-%d")

                if from_date > to_date:
                    from_date, to_date = to_date, from_date

                query += " AND order_date BETWEEN :from_date AND :to_date"
                params['from_date'] = from_date
                params['to_date'] = to_date


            # Execute the query with parameters
            orders = conn.execute(text(query), params)

            # Map the results to Order objects
            for order in orders:
                orders_objects.append(cls(
                    id=order[0],
                    customer_id=order[1],
                    table_code=order[2],
                    payment_method_id=order[3],
                    order_date=order[4]
                ))

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
                       table_code=order[2], payment_method_id=order[3],
                       order_date=order[4])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
