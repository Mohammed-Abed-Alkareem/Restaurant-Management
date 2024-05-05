import bcrypt

from . import *

class Employee():
    def __init__(self, *args):
        if len(args) == 4:
            self.id = generate_key('E')
            self.name = args[0]
            self.phone_number = args[1]
            self.password = Employee.hash_password(args[2])
            self.position = args[3]
        else:
            self.id = args[0]
            self.name = args[1]
            self.phone_number = args[2]
            self.password = Employee.hash_password(args[3])
            self.position = args[4]

    @staticmethod
    def create_table():
        conn = engine.connect()

        try:
            conn.execute(CREATE_EMPLOYEES_TABLE)
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
            conn.execute(DROP_EMPLOYEES_TABLE)
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()


    @staticmethod
    def hash_password(password):  # hash the password to 60 characters
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

