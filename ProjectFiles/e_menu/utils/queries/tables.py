from sqlalchemy import text

CREATE_TABLES_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS tables(
                            code INTEGER PRIMARY KEY,
                            location VARCHAR(200) NOT NULL,
                            type VARCHAR(50),
                            seats INTEGER NOT NULL
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
                        (code, location, type, seats)
                        VALUES (:code, :location, :type, :seats);
                    """)

SELECT_TABLE_BY_ID = text("""
                                SELECT * FROM tables 
                                WHERE code = :code;
                            """)

DELETE_FROM_TABLES = text("""
                                DELETE FROM tables 
                                WHERE code = :code;
                        """)

UPDATE_LOCATION_IN_TABLE = text("""
                            UPDATE menuItems  
                            SET location = :location 
                            WHERE code = :code;
                        """)

UPDATE_TYPE_IN_TABLE = text("""
                            UPDATE menuItems  
                            SET type = :type 
                            WHERE code = :code;
                        """)

UPDATE_SEATS_IN_TABLE = text("""
                            UPDATE menuItems  
                            SET seats = :seats 
                            WHERE code = :code;
                        """)
