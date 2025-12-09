1# Write your MySQL query statement below
2SELECT
3    p.product_name,
4    s.year,
5    s.price
6FROM Sales AS s
7JOIN Product AS p
8    ON s.product_id = p.product_id;
9