from sqlalchemy import text

CREATE_RATINGS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS ratings(
                            id CHAR(6) PRIMARY KEY,
                            order_id CHAR(6),
                            rating int,
                            food_rating int,
                            service_rating int,
                            FOREIGN KEY (order_id) REFERENCES orders(id)
                            );
                        """)

INSERT_INTO_RATINGS_TABLE = text("""
                                INSERT INTO ratings(id, order_id, rating, food_rating, service_rating) 
                                VALUES (:id, :order_id, :rating, :food_rating, :service_rating);
                            """)

SELECT_RATINGS_TABLE = text("""
                                    SELECT * FROM ratings
                                """)

GET_RATINGS_BY_ORDER_ID = text("""
                                    SELECT * FROM ratings
                                    WHERE order_id = :order_id;
                                """)

DROP_RATINGS_TABLE = text("""
                                DROP TABLE IF EXISTS ratings;
                            """)
