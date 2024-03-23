from sqlalchemy import create_engine
import urllib.parse
from ProjectFiles.e_menu.utils.queries.menuItems import *

encoded_password = urllib.parse.quote_plus('mosatukba1')

DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'


class MenuItems:
    def __init__(self, itemId, item_name, item_description, item_category, item_price):
        self.itemId = itemId
        self.item_name = item_name
        self.item_description = item_description
        self.item_category = item_category
        self.item_price = item_price

    def insert(self):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()

        try:
            conn.execute(INSERT_INTO_MENU_ITEMS,
                         {'itemId': self.itemId, 'item_name': self.item_name,
                          'item_description': self.item_description, 'item_category': self.item_category,
                          'item_price': self.item_price})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def delete(cls, itemId):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()
        try:
            conn.execute(DELETE_FROM_MENU_ITEMS, {'itemId': itemId})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def update(self, item_id, name, price, description, in_stock, category):
        pass

    @classmethod
    def get(cls, itemId):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()
        try:
            item = conn.execute(SELECT_ITEM_BY_ID, {'itemId': itemId}).fetchone()
            return cls(itemId=item[0], item_name=item[1], item_description=item[2],
                       item_category=item[3], item_price=item[4])
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
            items_objects = []
            items = conn.execute(SELECT_MENU_ITEMS).fetchall()
            for item in items:
                items_objects.append(cls(itemId=item[0], item_name=item[1], item_description=item[2],
                                         item_category=item[3], item_price=item[4]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_category(cls, category_id):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()
        try:
            items_objects = []
            items = conn.execute(SELECT_MENU_ITEMS_BY_CATEGORY, {'item_category': category_id}).fetchall()
            for item in items:
                items_objects.append(cls(itemId=item[0], item_name=item[1], item_description=item[2],
                                         item_category=item[3], item_price=item[4]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
