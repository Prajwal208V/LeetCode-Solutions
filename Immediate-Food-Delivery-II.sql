1-- Write your PostgreSQL query statement below
2SELECT ROUND(
3    AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 
4    2
5) AS immediate_percentage
6FROM (
7    SELECT *,
8           RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rk
9    FROM Delivery
10) t
11WHERE rk = 1;