1-- Write your PostgreSQL query statement below
2SELECT p.product_id, -- select product id
3ROUND(
4    COALESCE(SUM(u.units * p.price)::decimal / NULLIF(SUM(u.units), 0), 0), 
5    2
6) AS average_price -- weighted average price
7FROM Prices p
8LEFT JOIN UnitsSold u
9ON p.product_id = u.product_id -- match sales to prices
10AND u.purchase_date BETWEEN p.start_date AND p.end_date -- valid price period
11GROUP BY p.product_id; -- group per product