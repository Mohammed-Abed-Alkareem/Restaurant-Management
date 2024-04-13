from sqlalchemy import text

CREATE_ORDER_DETAILS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS orderDetails(
                            id CHAR(7) PRIMARY KEY,
                            order_id CHAR(6),
                            item_id CHAR(4),
                            price DOUBLE NOT NULL,
                            quantity int,
                            FOREIGN KEY (order_id) REFERENCES orders(id),
                            FOREIGN KEY (item_id) REFERENCES menuItems(id)
                            );
                        """)

INSERT_INTO_ORDER_DETAILS_TABLE = text("""
                                INSERT INTO orderDetails(id, order_id, item_id, price, quantity) 
                                VALUES (:id, :order_id, :item_id, :price, :quantity);
                            """)
DROP_ORDER_DETAILS_TABLE = text("""
                                DROP TABLE IF EXISTS orderDetails;
                            """)


GET_ORDER_DETAILS_TABLE = text("""
                        SELECT * FROM orderDetails
                    """)

GET_ORDER_DETAIL_BY_ORDER_ID = text("""
                        SELECT * FROM orderDetails
                        WHERE order_id = :order_id
                    """)

GET_ORDER_DETAILS_BY_ITEM_ID = text("""
                        SELECT * FROM orderDetails
                        WHERE item_id = :item_id
                    """)



