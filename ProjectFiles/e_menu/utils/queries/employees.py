from sqlalchemy import text

CREATE_EMPLOYEES_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS employees(
                            id CHAR(9) PRIMARY KEY,
                            name VARCHAR(40) NOT NULL,
                            phone_number CHAR(10) NOT NULL,
                            salary integer,
                            position VARCHAR(20) NOT NULL,
                            password CHAR(60) NOT NULL
                            );
                        """)

DROP_EMPLOYEES_TABLE = text("""
                            DROP TABLE IF EXISTS employees;
                        """)

INSERT_INTO_EMPLOYEES = text("""
                            INSERT INTO employees
                            (id, name, phone_number, salary, password, position)
                            VALUES (:id, :name, :phone_number, :salary, :password, :position);
                        """)

GET_EMPLOYEES_TABLE = text("""
                            SELECT * FROM employees ;
                        """)

SELECT_EMPLOYEE_BY_ID = text("""
                                SELECT * FROM employees
                                WHERE id = :id;
                            """)

SELECT_EMPLOYEE_BY_PHONE = text("""
                                SELECT * FROM employees
                                WHERE phone_number = :phone_number;
                            """)

DELETE_FROM_EMPLOYEES = text("""
                                DELETE FROM employees
                                WHERE id = :id;
                            """)

UPDATE_EMPLOYEE = text("""
                            UPDATE employees
                            SET name = :name, phone_number = :phone_number, password = :password, position = :position
                            WHERE id = :id;
                        """)

GET_EMPLOYEE_POSITION = text("""
                            SELECT position FROM employees
                            WHERE id = :id;
                        """)

GET_EMPLOYEES_TABLE_REVERSED = text(""" 
                            SELECT * FROM employees 
                            ORDER BY id DESC
                            LIMIT 1;
                        """)


