from sqlalchemy import text

CREATE_PAYMENT_METHODS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS paymentMethods(
                            id CHAR(32) PRIMARY KEY,
                            description VARCHAR(1000)
                            );
                        """)

SELECT_PAYMENT_METHODS_TABLE = text("""
                            SELECT * FROM paymentMethods;
                        """)

DROP_PAYMENT_METHODS_TABLE = text("""
                                DROP TABLE IF EXISTS paymentMethods;
                            """)

INSERT_INTO_PAYMENT_METHODS_TABLE = text("""
                            INSERT INTO paymentMethods 
                            (id, description) 
                            VALUES (:id, :description);
                        """)
