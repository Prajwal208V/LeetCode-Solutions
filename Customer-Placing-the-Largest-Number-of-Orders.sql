1# Write your MySQL query statement below
2SELECT customer_number -- select customer with most orders
3FROM Orders
4GROUP BY customer_number -- group orders per customer
5ORDER BY COUNT(*) DESC -- sort by order count descending
6LIMIT 1; -- pick the top customer