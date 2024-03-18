from sqlalchemy import text


CREATE_CUSTOMERS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS customers(
                            customerId char(5) PRIMARY KEY,
                            customer_name varchar(40) NOT NULL,
                            customer_phoneNumber char(10) NOT NULL
                            );
                        """)


DROP_CUSTOMERS_TABLE = text("""
                                DROP TABLE IF EXISTS customers;
                            """)


INSERT_CUSTOMERS_TABLE = text("""
                                INSERT INTO customers (customerId, customer_name, customer_phoneNumber) 
                                VALUES (:customerId, :customer_name, :customer_phoneNumber);
                            """)

##this for key
GET_CUSTOMERS_TABLE = text("""
                            Select * from customers order by 1 DESC;
""")


