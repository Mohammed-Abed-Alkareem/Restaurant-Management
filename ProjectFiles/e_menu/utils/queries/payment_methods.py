from sqlalchemy import text

CREATE_PAYMENT_METHODS_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS paymentMethods(
                            id CHAR(4) PRIMARY KEY,
                            description VARCHAR(32)
                            );
                        """)

SELECT_PAYMENT_METHODS_TABLE = text("""
                            SELECT * FROM paymentMethods;
                        """)

INSERT_INTO_PAYMENT_METHODS_TABLE = text("""
                            INSERT INTO paymentMethods 
                            (id, description) 
                            VALUES (:id, :description);
                        """)
