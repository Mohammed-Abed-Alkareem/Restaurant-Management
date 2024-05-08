from . import *


class Table:
    def __init__(self, *args):
        if len(args) == 4:
            self.code = args[0]
            self.location = args[1].strip()
            self.type = args[2].strip()
            self.seats = args[3]
        else:
            self.code = generate_key('T')
            self.location = args[0].strip()
            self.type = args[1].strip()
            self.seats = args[2]

    @staticmethod
    def create_table():
        conn = engine.connect()
        try:
            conn.execute(CREATE_TABLES_TABLE)
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
            conn.execute(DROP_TABLES_TABLE)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def insert(self):
        conn = engine.connect()
        try:
            conn.execute(INSERT_INTO_TABLES,
                         {'code': self.code, 'location': self.location, 'type': self.type,
                          'seats': self.seats})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def delete(cls, code):
        conn = engine.connect()
        try:
            conn.execute(DELETE_FROM_TABLES, {'code': code})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @classmethod
    def get(cls, code):
        conn = engine.connect()
        try:
            table = conn.execute(SELECT_TABLE_BY_ID, {'code': code}).fetchone()
            return cls(table[0], table[1], table[2], table[3])
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        conn = engine.connect()
        try:
            tables_objects = []
            tables = conn.execute(SELECT_TABLES).fetchall()
            for table in tables:
                tables_objects.append(cls(table[0], table[1], table[2], table[3]))
            return tables_objects
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    def to_dict(self):
        return {
            'code': self.code,
            'location': self.location,
            'type': self.type,
            'seats': self.seats
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            code=data_dict['code'],
            location=data_dict['location'],
            type=data_dict['type'],
            seats=data_dict['seats']
        )

    @classmethod
    def change_location(cls, table_code, new_location):
        conn = engine.connect()
        try:
            conn.execute(UPDATE_LOCATION_IN_TABLE,
                         {'code': table_code, 'location': new_location})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def change_type(cls, table_code, new_type):
        conn = engine.connect()
        try:
            conn.execute(UPDATE_TYPE_IN_TABLE,
                         {'code': table_code, 'type': new_type})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def change_seats(cls, table_code, new_seats):
        conn = engine.connect()
        try:
            conn.execute(UPDATE_SEATS_IN_TABLE,
                         {'code': table_code, 'seats': new_seats})
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
