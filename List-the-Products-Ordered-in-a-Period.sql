1-- Write your PostgreSQL query statement below
2SELECT p.product_name, SUM(o.unit) AS unit -- total units ordered
3FROM Products p
4JOIN Orders o ON p.product_id = o.product_id -- join orders with products
5WHERE o.order_date BETWEEN DATE '2020-02-01' AND DATE '2020-02-29' -- February 2020
6GROUP BY p.product_name -- group by product
7HAVING SUM(o.unit) >= 100; -- only products with at least 100 units