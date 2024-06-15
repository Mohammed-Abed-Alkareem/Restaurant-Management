from . import *


class Rating:
    def __init__(self,  order_id, rating, food_rating, service_rating, id=None):
        if id is None:
            id = generate_key('R')

        self.id = id
        self.order_id = order_id
        self.rating = rating
        self.food_rating = food_rating
        self.service_rating = service_rating

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_RATINGS_TABLE,
                         {'id': self.id, 'order_id': self.order_id,
                          'rating': self.rating, 'food_rating': self.food_rating, 'service_rating': self.service_rating})
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
            conn.execute(CREATE_RATINGS_TABLE)
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
            conn.execute(DROP_RATINGS_TABLE)
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
            ratings = conn.execute(SELECT_RATINGS_TABLE).fetchall()
            for rating in ratings:
                ratings_objects.append(cls(id=rating[0], order_id=rating[1],
                                           rating=rating[2], food_rating=rating[3], service_rating=rating[4]))
            return ratings_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_order_id(cls, order_id):
        conn = engine.connect()
        try:
            ratings_objects = []
            ratings = conn.execute(GET_RATINGS_BY_ORDER_ID).fetchall()
            for rating in ratings:
                ratings_objects.append(cls(id=rating[0], order_id=rating[1],
                                           rating=rating[2], food_rating=rating[3], service_rating=rating[4]))
            return ratings_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
