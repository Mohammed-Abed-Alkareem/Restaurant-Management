from sqlalchemy import text

CREATE_MENU_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS menuItems(
                            itemId INTEGER PRIMARY KEY,
                            name varchar(50) NOT NULL,
                            description varchar(200),
                            category varchar(50) NOT NULL,
                            price DOUBLE NOT NULL
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
                            ( itemId, name, description, category, price) 
                            VALUES ( :itemId, :name, :description, :category, :price);
                        """)

UPDATE_PRICE_IN_MENU_ITEMS = text("""
                            UPDATE menuItems  
                            SET price = :price 
                            WHERE itemId = :itemId;
                        """)

DELETE_FROM_MENU_ITEMS = text("""
                                DELETE FROM menuItems 
                                WHERE itemId = :itemId; 
                        """)

SELECT_MENU_ITEMS_BY_CATEGORY = text("""
                                        SELECT * FROM menuItems 
                                        WHERE category = :category
                                    """)

GET_CATEGORIES_IN_MENU_ITEMS = text("""
                                    SELECT category FROM menuItems
                                    GROUP BY category;
                                """)

