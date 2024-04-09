from . import *


class Rating:
    def __init__(self, id, order_id, customer_id, rating, food_rating, service_rating):
        self.id = id
        self.order_id = order_id
        self.customer_id = customer_id
        self.rating = rating
        self.food_rating = food_rating
        self.service_rating = service_rating

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_RATINGS_TABLE,
                         {'id': self.id, 'order_id': self.order_id, 'customer_id': self.customer_id,
                          'rating': self.rating, 'food_rating': self.food_rating, 'service_rating': self.service_rating})
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
            ratings_objects = []
            ratings = conn.execute(SELECT_PAYMENT_METHODS_TABLE).fetchall()
            for rating in ratings:
                ratings_objects.append(cls(id=rating[0], order_id=rating[1], customer_id=rating[2],
                                           rating=rating[3], food_rating=rating[4], service_rating=rating[5]))
            return ratings_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_customer_id(cls, customer_id):
        conn = engine.connect()
        try:
            ratings_objects = []
            ratings = conn.execute(GET_RATINGS_BY_CUSTOMER_ID).fetchall()
            for rating in ratings:
                ratings_objects.append(cls(id=rating[0], order_id=rating[1], customer_id=rating[2],
                                           rating=rating[3], food_rating=rating[4], service_rating=rating[5]))
            return ratings_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
