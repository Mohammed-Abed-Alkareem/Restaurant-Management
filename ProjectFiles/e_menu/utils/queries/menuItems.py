from sqlalchemy import text

CREATE_MENU_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS menuItems(
                            id CHAR(4) PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            description VARCHAR(1000),
                            category VARCHAR(50) NOT NULL,
                            price DOUBLE NOT NULL,
                            is_available BOOLEAN,
                            cuisine_type varchar(20)
                            );
                        """)

DROP_MENU_TABLE = text("""
                            DROP TABLE IF EXISTS menuItems;
                        """)

SELECT_MENU_ITEMS = text("""
                            SELECT * FROM menuItems;
                        """)

INSERT_INTO_MENU_ITEMS = text("""
                            INSERT INTO menuItems 
                            (id, name, description, category, price, is_available, cuisine_type) 
                            VALUES (:id, :name, :description, :category, :price, :is_available, :cuisine_type);
                        """)

UPDATE_PRICE_IN_MENU_ITEMS = text("""
                            UPDATE menuItems  
                            SET price = :price 
                            WHERE id = :id;
                        """)

DELETE_FROM_MENU_ITEMS = text("""
                                DELETE FROM menuItems 
                                WHERE id = :id; 
                        """)

SELECT_MENU_ITEMS_BY_CATEGORY = text("""
                                        SELECT * FROM menuItems 
                                        WHERE category = :category;
                                    """)

GET_CATEGORIES_IN_MENU_ITEMS = text("""
                                    SELECT category FROM menuItems
                                    GROUP BY category;
                                """)

SELECT_MENU_ITEM_BY_ID = text("""
                                SELECT * FROM menuItems
                                WHERE id = :id;
                            """)

GET_MENU_ITEMS_TABLE = text("""
                            SELECT * FROM menuItems ORDER BY 1 DESC;
""")

UPDATE_MENU_ITEM = text("""
                            UPDATE menuItems
                            SET name = :name, price = :price, 
                                description = :description, category = :category, 
                                is_available = :is_available
                            WHERE id = :id;
                        """)

CHANGE_AVAILIBILITY = text("""
                            UPDATE menuItems
                            SET is_available = :is_available
                            WHERE id = :id;
                        """)
