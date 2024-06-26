from sqlalchemy import text

CREATE_CUSTOMERS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS customers(
                            id char(5) PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            phone_number char(10) NOT NULL UNIQUE,
                            gender varchar(10),
                            birth_year int,
                            favourite_cuisine varchar(20)
                            );
                        """)

DROP_CUSTOMERS_TABLE = text("""
                                DROP TABLE IF EXISTS customers;
                            """)

INSERT_CUSTOMERS_TABLE = text("""
                                INSERT INTO customers (id, name, phone_number, gender, birth_year, favourite_cuisine) 
                                VALUES (:id, :name, :phone_number, :gender, :birth_year, :favourite_cuisine);
                            """)

GET_CUSTOMERS_TABLE = text("""
                            SELECT * FROM customers ORDER BY 1 DESC;
""")

SELECT_CUSTOMER_BY_ID = text("""
                                SELECT * FROM customers
                                WHERE id = :id;
                            """)

SELECT_CUSTOMER_BY_PHONE = text("""
                                SELECT * FROM customers
                                WHERE phone_number = :phone_number;
                            """)

DELETE_FROM_CUSTOMERS = text("""
                                DELETE FROM customers 
                                WHERE id = :id;
                            """)
