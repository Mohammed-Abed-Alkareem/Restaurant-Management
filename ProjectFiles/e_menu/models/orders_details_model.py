from . import *


class OrderDetails:
    def __init__(self, order_id, item_id, price, quantity, id=None):
        if id is None:
            id = generate_key('D')

        self.id = id
        self.order_id = order_id
        self.item_id = item_id
        self.price = price
        self.quantity = quantity
    # def __init__(self, *args):
    #
    #     if len(args) == 4:
    #         self.id = generate_key('D')
    #         self.order_id = args[0]
    #         self.item_id = args[1]
    #         self.price = args[2]
    #         self.quantity = args[3]
    #
    #     else:
    #         self.id = args[0]
    #         self.order_id = args[1]
    #         self.item_id = args[2]
    #         self.price = args[3]
    #         self.quantity = args[4]


    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_ORDER_DETAILS_TABLE,
                         {'id': self.id, 'order_id': self.order_id, 'item_id': self.item_id, 'price': self.price,
                          'quantity': self.quantity})
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
            conn.execute(CREATE_ORDER_DETAILS_TABLE)
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
            conn.execute(DROP_ORDER_DETAILS_TABLE)
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get_by_order_id(cls, order_id):
        conn = engine.connect()
        try:
            order_detail = conn.execute(GET_ORDER_DETAIL_BY_ORDER_ID, {'order_id': order_id}).fetchone()
            return cls(id=order_detail[0], order_id=order_detail[1],
                       item_id=order_detail[2], price=order_detail[3],
                       quantity=order_detail[4])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        conn = engine.connect()
        try:
            order_details_objects = []
            order_details = conn.execute(GET_ORDER_DETAILS_TABLE).fetchall()
            for order_detail in order_details:
                order_details_objects.append(cls(id=order_detail[0], order_id=order_detail[1],
                                                 item_id=order_detail[2], price=order_detail[3],
                                                 quantity=order_detail[4]))
            return order_details_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_item_id(cls, item_id):
        conn = engine.connect()
        try:
            order_details_objects = []
            order_details = conn.execute(GET_ORDER_DETAILS_BY_ITEM_ID, {'item_id': item_id}).fetchall()
            for order_detail in order_details:
                order_details_objects.append(cls(id=order_detail[0], order_id=order_detail[1],
                                                 item_id=order_detail[2], price=order_detail[3],
                                                 quantity=order_detail[4]))
            return order_details_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
