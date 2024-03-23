from sqlalchemy import create_engine
import urllib.parse
# from ...utils.queries.menuItems import *
#from ...utils.queries.tables import *
from ProjectFiles.e_menu.utils.queries.tables import *
# from ...utils.queries.customers import *
# from ...utils.read_initial_data import *

# Encode the password
encoded_password = urllib.parse.quote_plus('mosatukba1')
# Construct the connection string
DATABASE = f'mysql+pymysql://root:{encoded_password}@127.0.0.1/e_menu'


class Table:
    def __init__(self, code: int, seats: int, location: str, type: str):
        self.code = code
        self.seats = seats
        self.location = location
        self.type = type

    def insert(self):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()

        try:
            conn.execute(INSERT_INTO_TABLES,
                         {'tableId': self.code, 'location': self.location, 'class': self.type,
                          'numOfSeats': self.seats})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()


    @classmethod
    def delete(cls, table_code):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()
        try:
            conn.execute(DELETE_FROM_TABLES, {'tableId': table_code})
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    def update(self, table_code, number_of_seats, location, table_type):
        pass

    @classmethod
    def get(cls, table_code):
        engine = create_engine(DATABASE, echo=True)
        conn = engine.connect()
        try:
            table = conn.execute(SELECT_TABLE_BY_ID, {'tableId': int(table_code)}).fetchone()
            return cls(code=table[0], location=table[1], type=table[2], seats=table[3])
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


if __name__ == '__main__':
    Table.get_all()
