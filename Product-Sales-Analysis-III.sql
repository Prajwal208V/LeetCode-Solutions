1-- Write your PostgreSQL query statement below
2SELECT product_id, 
3       year AS first_year, 
4       quantity, 
5       price
6FROM (
7    SELECT *, 
8           RANK() OVER (PARTITION BY product_id ORDER BY year) AS rk
9    FROM Sales
10) t
11WHERE rk = 1;