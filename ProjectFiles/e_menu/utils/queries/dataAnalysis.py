from sqlalchemy import text

# ╔════════════════════════════════╗
# ║                                ║
# ║            Mohammed            ║
# ║                                ║
# ╚════════════════════════════════╝

visit_frequency = text("""
SELECT c.name, COUNT(o.id) AS visit_count
FROM customers AS c
JOIN orders AS o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY visit_count DESC
""")


spending_patterns = text("""
SELECT c.name, SUM(od.price * od.quantity) AS total_spent
FROM customers AS c
JOIN orders AS o ON c.id = o.customer_id
JOIN orderDetails AS od ON o.id = od.order_id
GROUP BY c.id, c.name
ORDER BY total_spent DESC
""")


best_selling_items = text("""
SELECT m.name, COUNT(od.quantity) AS count
FROM menuItems AS m
JOIN orderDetails AS od ON m.id = od.item_id
GROUP BY m.name
ORDER BY count DESC
""")


yearly_sales = text("""
SELECT YEAR(o.order_date) AS year, SUM(od.price * od.quantity) AS total
FROM orders AS o
JOIN orderDetails AS od ON o.id = od.order_id
GROUP BY year
ORDER BY year
""")

#Mohammed
table_location_ratings = text("""
    SELECT t.location, AVG(r.rating) AS average_rating,
     AVG(r.food_rating) AS average_food_rating, AVG(r.service_rating) AS average_service_rating
    FROM Tables t
    JOIN Orders o ON t.code = o.table_code
    JOIN Ratings r ON o.id = r.order_id
    GROUP BY t.location
""")


#Mohammed
most_profitable_items = text("""
    SELECT mi.name AS item_name, SUM(od.quantity * od.price) AS total_revenue, AVG(r.rating) AS average_rating
    FROM MenuItems mi
    JOIN OrderDetails od ON mi.id = od.item_id
    JOIN Orders o ON od.order_id = o.id
    JOIN Ratings r ON o.id = r.order_id
    GROUP BY mi.name
    ORDER BY total_revenue DESC
""")

#*****************************************************************************************
#*****************************************************************************************


gender_distribution = text("""
SELECT gender, COUNT(*) AS count
FROM customers
GROUP BY gender
""")

age_distribution = text("""
SELECT (YEAR(CURDATE()) - birth_year) AS age, COUNT(*) AS count
FROM customers
GROUP BY age
""")

favorite_cuisine_preferences = text("""
SELECT favourite_cuisine, COUNT(*) AS count
FROM customers
GROUP BY favourite_cuisine
""")



category_performance = text("""
SELECT m.category, SUM(od.price * od.quantity) AS total
FROM menuItems AS m
JOIN orderDetails AS od ON m.id = od.item_id
GROUP BY m.category
""")



monthly_sales = text("""
SELECT MONTH(o.order_date) AS month, SUM(od.price * od.quantity) AS total
FROM orders AS o
JOIN orderDetails AS od ON o.id = od.order_id
GROUP BY month
ORDER BY month
""")

peak_hours = text("""
SELECT EXTRACT(HOUR FROM o.order_date) AS hour, COUNT(*) / COUNT(DISTINCT DATE(o.order_date)) AS avg_orders
FROM orders o
GROUP BY hour
ORDER BY avg_orders DESC, hour DESC
LIMIT 3
""")

popular_menu_items = text("""
SELECT m.name, COUNT(*) AS order_count
FROM menuItems as m
JOIN orderDetails as od
ON m.id = od.item_id
GROUP BY m.name
ORDER BY order_count DESC
LIMIT 10
""")


rating_trends = text("""
SELECT DATE(o.order_date) AS rating_date, AVG(r.rating) AS avg_rating
FROM ratings AS r
JOIN orders AS o ON o.id = r.order_id
GROUP BY rating_date
ORDER BY rating_date
""")

food_vs_service_ratings = text("""
SELECT AVG(r.food_rating) AS food_rating, AVG(r.service_rating) AS service_rating
FROM ratings AS r
""")

popular_payment_methods = text("""
SELECT payment_method_id, COUNT(*) AS method_count
FROM orders
GROUP BY payment_method_id
ORDER BY method_count DESC
""")

payment_trends = text("""
SELECT DATE(o.order_date) AS payment_date, o.payment_method_id, COUNT(*) AS method_count
FROM orders AS o
GROUP BY payment_date, o.payment_method_id
ORDER BY payment_date, o.payment_method_id
""")




payment_methods_impact = text("""
    SELECT pm.id AS payment_method, AVG(od.quantity * od.price) AS average_order_value,
     COUNT(o.id) AS order_count, AVG(r.rating) AS average_rating
    FROM PaymentMethods pm
    JOIN Orders o ON pm.id = o.payment_method_id
    JOIN OrderDetails od ON o.id = od.order_id
    JOIN Ratings r ON o.id = r.order_id
    GROUP BY pm.id
""")


time_categorized_orders = text("""
    WITH TimeCategorizedOrders AS (
        SELECT o.id, 
               CASE 
                   WHEN EXTRACT(HOUR FROM o.order_date) BETWEEN 6 AND 10 THEN 'Breakfast'
                   WHEN EXTRACT(HOUR FROM o.order_date) BETWEEN 11 AND 14 THEN 'Lunch'
                   WHEN EXTRACT(HOUR FROM o.order_date) BETWEEN 18 AND 21 THEN 'Dinner'
                   ELSE 'Other'
               END AS time_of_day
        FROM Orders o
    ),
    ItemOrderCounts AS (
        SELECT tco.time_of_day, mi.name AS item_name, COUNT(od.item_id) AS order_count
        FROM TimeCategorizedOrders tco
        JOIN OrderDetails od ON tco.id = od.order_id
        JOIN menuItems mi ON od.item_id = mi.id
        WHERE tco.time_of_day IN ('Breakfast', 'Lunch', 'Dinner')
        GROUP BY tco.time_of_day, mi.name
    )
    SELECT io.time_of_day, io.item_name, io.order_count
    FROM ItemOrderCounts io
    WHERE io.order_count = (
        SELECT MAX(order_count)
        FROM ItemOrderCounts sub_io
        WHERE sub_io.time_of_day = io.time_of_day
    )
    ORDER BY io.order_count, io.time_of_day 
""")

cohort_analysis = text("""
    WITH FirstOrder AS (
        SELECT customer_id, MIN(order_date) AS first_order_date
        FROM Orders
        GROUP BY customer_id
    ),
    CohortData AS (
        SELECT c.id, fo.first_order_date, o.order_date,
               TIMESTAMPDIFF(MONTH, fo.first_order_date, o.order_date) AS cohort_month
        FROM Customers c
        JOIN FirstOrder fo ON c.id = fo.customer_id
        JOIN Orders o ON c.id = o.customer_id
    )
    SELECT cohort_month, COUNT(DISTINCT cd.id) AS customer_count,
     AVG(od.quantity * mi.price) AS average_order_value, AVG(r.rating) AS average_rating
    FROM CohortData cd
    JOIN Orders o ON cd.id = o.customer_id
    JOIN OrderDetails od ON o.id = od.order_id
    JOIN MenuItems mi ON od.item_id = mi.id
    JOIN Ratings r ON o.id = r.order_id
    GROUP BY cohort_month
    ORDER BY cohort_month
""")


customer_lifetime_value = text("""
    WITH CustomerOrders AS (
        SELECT c.id AS customer_id, 
               o.id AS order_id,
               SUM(od.quantity * mi.price) AS order_value
        FROM Customers c
        JOIN Orders o ON c.id = o.customer_id
        JOIN OrderDetails od ON o.id = od.order_id
        JOIN MenuItems mi ON od.item_id = mi.id
        GROUP BY c.id, o.id
    ),
    CustomerRevenue AS (
        SELECT customer_id, SUM(order_value) AS total_revenue
        FROM CustomerOrders
        GROUP BY customer_id
    )
    SELECT cr.customer_id, c.name, cr.total_revenue
    FROM CustomerRevenue cr
    JOIN Customers c ON cr.customer_id = c.id
    ORDER BY cr.total_revenue DESC
""")
