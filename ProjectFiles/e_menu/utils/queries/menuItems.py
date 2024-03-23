from sqlalchemy import text

CREATE_MENU_TABLE = text("""
                            CREATE TABLE IF NOT EXISTS menuItems(
                            itemId char(4) PRIMARY KEY,
                            item_name varchar(50) NOT NULL,
                            item_description varchar(200),
                            item_category varchar(50) NOT NULL,
                            item_price DOUBLE NOT NULL
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
                            ( itemId, item_name, item_description, item_category, item_price) 
                            VALUES ( :itemId, :item_name, :item_description, :item_category, :item_price);
                        """)

UPDATE_PRICE_IN_MENU_ITEMS = text("""
                            UPDATE menuItems  
                            SET item_price = :item_price 
                            WHERE itemId = :itemId;
                        """)

DELETE_FROM_MENU_ITEMS = text("""
                                DELETE FROM menuItems 
                                WHERE itemId = :itemId; 
                        """)

SELECT_MENU_ITEMS_BY_CATEGORY = text("""
                                        SELECT * FROM menuItems 
                                        WHERE item_category = :item_category
                                    """)

GET_CATEGORIES_IN_MENU_ITEMS = text("""
                                    SELECT item_category FROM menuItems
                                    GROUP BY item_category;
                                """)

SELECT_ITEM_BY_ID = text("""
                                SELECT * FROM menuItems
                                WHERE itemId = :itemId;
                            """)
