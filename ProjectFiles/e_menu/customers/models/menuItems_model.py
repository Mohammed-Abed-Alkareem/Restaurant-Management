from . import *


class MenuItems:
    def __init__(self, *args, **kwargs):
        if len(args) == 5:
            self.id = args[0].strip()
            self.name = args[1].strip()
            self.description = args[2].strip()
            self.category = args[3].strip()
            self.price = args[4]
        else:
            self.id = generate_key('M')
            self.name = args[0].strip()
            self.description = args[1].strip()
            self.category = args[2].strip()
            self.price = args[3]

        if kwargs:
            self.is_available = kwargs['is_available']
        else:
            self.is_available = True

    @staticmethod
    def create_table():
        conn = engine.connect()
        try:
            conn.execute(CREATE_MENU_TABLE)
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
            conn.execute(DROP_MENU_TABLE)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_MENU_ITEMS,
                         {'id': self.id, 'name': self.name,
                          'description': self.description, 'category': self.category,
                          'price': self.price, 'is_available': self.is_available})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def update(cls, id, name, price, description, category, is_available):
        conn = engine.connect()
        try:
            conn.execute(UPDATE_MENU_ITEM,
                         {'name': name, 'price': price, 'description': description,
                          'category': category, 'is_available': is_available, 'id': id})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def delete(cls, id):
        conn = engine.connect()
        try:
            conn.execute(DELETE_FROM_MENU_ITEMS, {'id': id})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def get(cls, id):
        conn = engine.connect()
        try:
            item = conn.execute(SELECT_MENU_ITEM_BY_ID, {'id': id}).fetchone()
            return cls(item[0], item[1], item[2], item[3], item[4], is_available=item[5])
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
                items_objects.append(cls(item[0], item[1], item[2], item[3], item[4], is_available=item[5]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_by_category(cls, category):
        conn = engine.connect()
        try:
            items_objects = []
            items = conn.execute(SELECT_MENU_ITEMS_BY_CATEGORY, {'category': category}).fetchall()
            for item in items:
                items_objects.append(cls(item[0], item[1], item[2], item[3], item[4], is_available=item[5]))
            return items_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_categories(cls):
        conn = engine.connect()
        try:
            rows = conn.execute(GET_CATEGORIES_IN_MENU_ITEMS)
            category_list = [category[0] for category in rows.fetchall()]
            return category_list
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            conn.close()
