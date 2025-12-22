1-- Write your PostgreSQL query statement below
2SELECT c.customer_id
3FROM Customer c
4JOIN Product p ON c.product_key = p.product_key
5GROUP BY c.customer_id
6HAVING COUNT(DISTINCT c.product_key) = (
7    SELECT COUNT(*) 
8    FROM Product
9);