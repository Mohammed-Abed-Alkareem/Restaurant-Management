from sqlalchemy import text

CREATE_ORDERS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS orders(
                            id CHAR(6) PRIMARY KEY,
                            customer_id CHAR(5),
                            table_code INTEGER,
                            payment_method_id CHAR(32),
                            order_date DATE,
                            FOREIGN KEY (customer_id) REFERENCES customers(id),
                            FOREIGN KEY (table_code) REFERENCES tables(code),
                            FOREIGN KEY (payment_method_id) REFERENCES paymentMethods(id)
                            );
                        """)

DROP_ORDERS_TABLE = text("""
                                DROP TABLE IF EXISTS orders;
                            """)


INSERT_INTO_ORDERS_TABLE = text("""
                                INSERT INTO orders(id, customer_id, table_code, payment_method_id, order_date) 
                                VALUES (:id, :customer_id, :table_code, :payment_method_id, :order_date);
                            """)

GET_ORDERS_TABLE = text("""
                        SELECT * FROM ORDERS
                    """)

GET_CUSTOMER_CURRENT_ORDER = text("""
                        SELECT * FROM ORDERS
                        WHERE customer_id = :customer_id
                        ORDER BY order_date DESC
                        LIMIT 1
                    """)


GET_TABLE_CURRENT_ORDER = text("""
                        SELECT * FROM ORDERS
                        WHERE table_code = :table_code
                        ORDER BY order_date DESC
                        LIMIT 1
                    """)

DROP_ORDERS_PAYMENT_CONSTRAINT = text("""
                                ALTER TABLE Orders DROP FOREIGN KEY orders_ibfk_3;
                                """)
DROP_ORDERS_CUSTOMER_CONSTRAINT = text("""
                                ALTER TABLE Orders DROP FOREIGN KEY customer_id;
                                """)

DROP_ORDERS_TABLE_CONSTRAINT = text("""
                                ALTER TABLE Orders DROP FOREIGN KEY table_code;
                                """)