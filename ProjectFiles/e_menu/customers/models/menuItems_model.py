from . import *


class MenuItems:
    def __init__(self, *args):

        if len(args) == 5:
            self.itemId = args[0].strip()
            self.item_name = args[1].strip()
            self.item_description = args[2].strip()
            self.item_category = args[3].strip()
            self.item_price = args[4]

        else:
            self.itemId = generate_key()
            self.item_name = args[0].strip()
            self.item_description = args[1].strip()
            self.item_category = args[2].strip()
            self.item_price = args[3]

    def insert(self):

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

        conn = engine.connect()
        try:

            item = conn.execute(SELECT_ITEM_BY_ID, {'itemId': itemId}).fetchone()
            return cls(item[0], item[1], item[2],
                       item[3], item[4])

        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):

        conn = engine.connect()
        try:
            items_objects = []
            items = conn.execute(SELECT_MENU_ITEMS).fetchall()
            for item in items:
                items_objects.append(cls(item[0], item[1], item[2],
                                         item[3], item[4]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_category(cls, category_id):
        conn = engine.connect()
        try:
            items_objects = []
            items = conn.execute(SELECT_MENU_ITEMS_BY_CATEGORY, {'item_category': category_id}).fetchall()
            for item in items:
                items_objects.append(cls(item[0], item[1], item[2],
                                         item[3], item[4]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def get_categories():
        conn = engine.connect()
        rows = conn.execute(GET_CATEGORIES_IN_MENU_ITEMS)

        category_list = [category[0] for category in rows.fetchall()]
        print(category_list)
        conn.close()
        return category_list
