from sqlalchemy import text

CREATE_ORDER_DETAILS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS orderDetails(
                            id CHAR(4) PRIMARY KEY,
                            order_id CHAR(4),
                            item_id CHAR(4),
                            price DOUBLE NOT NULL,
                            quantity int,
                            FOREIGN KEY (order_id) REFERENCES orders(id),
                            FOREIGN KEY (item_id) REFERENCES menuItems(id)
                            );
                        """)

INSERT_INTO_ORDER_DETAILS_TABLE = text("""
                                INSERT INTO orders(id, order_id, item_id, price, quantity) 
                                VALUES (:id, :order_id, :order_id, :item_id, :price, :quantity);
                            """)

GET_ORDER_DETAILS_TABLE = text("""
                        SELECT * FROM orderDetails
                    """)

GET_ORDER_DETAIL_BY_ORDER_ID = text("""
                        SELECT * FROM orderDetails
                        WHERE order_id = :order_id
                    """)

GET_ORDER_DETAILS_BY_ITEM_ID = text("""
                        SELECT * FROM ORDERS
                        WHERE item_id = :item_id
                    """)



