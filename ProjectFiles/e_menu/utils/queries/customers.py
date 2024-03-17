from sqlalchemy import text


CREATE_CUSTOMERS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS customers(
                            customerId char(5) PRIMARY KEY,
                            name varchar(20) NOT NULL,
                            phoneNumber char(10) NOT NULL
                            );
                        """)


DROP_CUSTOMERS_TABLE = text("""
                                DROP TABLE IF EXISTS customers;
                            """)


INSERT_CUSTOMERS_TABLE = text("""
                                INSERT INTO customers (customerId, name, phoneNumber) 
                                VALUES (:customerId, :name, :phoneNumber);
                            """)

GET_CUSTOMERS_TABLE = text("""
                            Select * from customers order by 1 DESC;
""")