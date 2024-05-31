from . import *


class MenuItems:

    def __init__(self, name, description, category, price, id=None, is_available=True, cuisine_type='Other'):
        if id is None:
            id = generate_key('M')

        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.is_available = is_available
        self.cuisine_type = cuisine_type

    # def __init__(self, *args):
    #
    #     if len(args) == 6:
    #         self.id = args[0].strip()
    #         self.name = args[1].strip()
    #         self.description = args[2].strip()
    #         self.category = args[3].strip()
    #         self.price = args[4]
    #         self.is_available = args[5]
    #     else:
    #         self.id = generate_key('M')
    #         self.name = args[0].strip()
    #         self.description = args[1].strip()
    #         self.category = args[2].strip()
    #         self.price = args[3]
    #         self.is_available = args[4]

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
                          'price': self.price, 'is_available': self.is_available,
                          'cuisine_type': self.cuisine_type})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def update(self, name=None, price=None, description=None, category=None, is_available=None, cuisine_type=None):
        name = self.name if name is None else name
        price = self.price if price is None else price
        description = self.description if description is None else description
        category = self.category if category is None else category
        is_available = self.is_available if is_available is None else is_available
        cuisine_type = self.cuisine_type if cuisine_type is None else cuisine_type
        conn = engine.connect()
        try:
            conn.execute(UPDATE_MENU_ITEM,
                         {'name': name, 'price': price, 'description': description,
                          'category': category, 'is_available': is_available,
                          'cuisine_type': cuisine_type, 'id': self.id})
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
            return cls(id=item[0], name=item[1], description=item[2],
                       category=item[3], price=item[4], is_available=item[5],
                       cuisine_type=item[6])
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
                items_objects.append(cls(id=item[0], name=item[1], description=item[2],
                                         category=item[3], price=item[4], is_available=item[5],
                                         cuisine_type=item[6]))
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
                if item[5] == True: # is_available is True
                    items_objects.append(cls(id=item[0], name=item[1], description=item[2],
                                             category=item[3], price=item[4], is_available=item[5],
                                             cuisine_type=item[6]))
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
            #remove spacing at begining and end of each category

            category_list = [row[0].strip() for row in rows]

            return category_list
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def change_availability(item_id):
        conn = engine.connect()
        try:
            item = conn.execute(SELECT_MENU_ITEM_BY_ID, {'id': item_id}).fetchone()
            is_available = not item[5]
            conn.execute(CHANGE_AVAILIBILITY, {'id': item_id, 'is_available': is_available})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
