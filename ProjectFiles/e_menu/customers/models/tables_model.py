from . import *


class Table:
    def __init__(self, code: int, location: str, type: str, seats: int):
        self.code = code
        self.location = location
        self.type = type
        self.seats = seats

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
            return cls(code=table[0], location=table[1], type=table[2], seats=table[3])
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
                tables_objects.append(cls(code=table[0], location=table[1], type=table[2], seats=table[3]))
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
