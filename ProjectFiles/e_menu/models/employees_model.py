import bcrypt

from . import *


class Employee:
    def __init__(self, name, phone_number, salary, position, password, id=generate_key('E')):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.salary = salary
        self.position = position
        self.password = Employee.hash_password(password)

    # def __init__(self, *args):
    #     if len(args) == 5:
    #         self.id = generate_key('E')
    #         self.name = args[0]
    #         self.phone_number = args[1]
    #         self.salary = args[2]
    #         self.position = args[3]
    #         self.password = Employee.hash_password(args[4])
    #     else:
    #         self.id = args[0]
    #         self.name = args[1]
    #         self.phone_number = args[2]
    #         self.salary = args[3]
    #         self.position = args[4]
    #         self.password = Employee.hash_password(args[5])


    def insert(self):
        conn = engine.connect()

        try:
            conn.execute(
                INSERT_INTO_EMPLOYEES,
                {'id': self.id,
                 'name': self.name,
                 'phone_number': self.phone_number,
                 'salary': self.salary,
                 'position': self.position,
                 'password': self.password}
            )
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = engine.connect()
        employees_info = []
        try:
            result = conn.execute(GET_EMPLOYEES_TABLE)
            employees = result.fetchall()
            print(employees)
            for employee in employees:
                employees_info.append(
                                    Employee(
                                        id=employee[0],
                                        name=employee[1],
                                        phone_number=employee[2],
                                        salary=employee[3],
                                        position=employee[4],
                                        password=employee[5]
                                    )
                )

            return employees_info

        except Exception as e:

            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def delete(employee_id):
        conn = engine.connect()

        try:
            conn.execute(DELETE_FROM_EMPLOYEES, id=employee_id)
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
    def get_by_phone_number(phone_number):
        conn = engine.connect()

        try:
            result = conn.execute(SELECT_EMPLOYEE_BY_PHONE, {'phone_number': phone_number})
            employee = result.fetchone()
            print(employee)
            return Employee(
                id=employee[0],
                name=employee[1],
                phone_number=employee[2],
                salary=employee[3],
                position=employee[4],
                password=employee[5]
            )

        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    def update(self, name=None, phone_number=None, salary=None, position=None, password=None):

        if name is None:
            name = self.name

        if phone_number is None:
            phone_number = self.phone_number

        if salary is None:
            salary = self.salary

        if position is None:
            position = self.position

        if password is None:
            password = self.password
        else:
            password = Employee.hash_password(password)

        conn = engine.connect()
        try:
            conn.execute(UPDATE_EMPLOYEE, {'id': id,
                                           'name': name,
                                           'phone_number': phone_number,
                                           'salary': salary,
                                           'position': position,
                                           'password': password}
                         )
            conn.commit()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            conn.close()


    @staticmethod
    def hash_password(password):  # hash the password to 60 characters
        return bcrypt.hashpw(str(password).encode('utf-8'), bcrypt.gensalt())