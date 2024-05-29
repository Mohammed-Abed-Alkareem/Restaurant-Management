from sqlalchemy import text

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
""")

best_selling_items = text("""
SELECT m.name, COUNT(od.quantity) AS count
FROM menuItems AS m
JOIN orderDetails AS od ON m.id = od.item_id
GROUP BY m.name
""")

category_performance = text("""
SELECT m.category, SUM(od.price * od.quantity) AS total
FROM menuItems AS m
JOIN orderDetails AS od ON m.id = od.item_id
GROUP BY m.category
""")

yearly_sales = text("""
SELECT YEAR(o.order_date) AS year, SUM(od.price * od.quantity) AS total
FROM orders AS o
JOIN orderDetails AS od ON o.id = od.order_id
GROUP BY year
""")

monthly_sales = text("""
SELECT YEAR(o.order_date) AS year, MONTH(o.order_date) AS month, SUM(od.price * od.quantity) AS total
FROM orders AS o
JOIN orderDetails AS od ON o.id = od.order_id
GROUP BY year, month
""")

peak_hours = text("""
SELECT EXTRACT(HOUR FROM o.order_date) AS hour, COUNT(*) / COUNT(DISTINCT DATE(o.order_date)) AS avg_orders
FROM orders o
GROUP BY hour
""")

popular_menu_items = text("""
SELECT m.name, COUNT(*) AS order_count
FROM menuItems as m
JOIN orderDetails as od
ON m.id = od.item_id
GROUP BY m.name
ORDER BY order_count DESC
""")

rating_trends = text("""
SELECT DATE(o.order_date) AS rating_date, AVG(r.rating) AS avg_rating
FROM ratings AS r
JOIN orders AS o ON o.id = r.order_id
GROUP BY rating_date
ORDER BY rating_date
""")

food_vs_service_ratings = text("""
SELECT AVG(r.food_rating) AS avg_food_rating, AVG(r.service_rating) AS avg_service_rating
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
