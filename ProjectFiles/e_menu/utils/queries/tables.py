from sqlalchemy import text

CREATE_TABLES_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS tables(
                            tableId INTEGER PRIMARY KEY,
                            location varchar(200) NOT NULL,
                            class varchar(50),
                            numOfSeats INTEGER NOT NULL
                            );
                        """)

DROP_TABLES_TABLE = text("""
                            DROP TABLE IF EXISTS tables;
                        """)

SELECT_TABLES = text("""
                        SELECT * FROM tables;
                    """)

INSERT_INTO_TABLES = text("""
                        INSERT INTO tables 
                        (tableId, location, class, numOfSeats)
                        VALUES (:tableId, :location, :class, :numOfSeats);
                    """)

SELECT_TABLE_BY_ID = text("""
                                SELECT * FROM tables 
                                WHERE tableId = :tableId;
                            """)