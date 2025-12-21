1-- Write your PostgreSQL query statement below
2SELECT customer_number -- select customer id
3FROM Orders
4GROUP BY customer_number -- group orders by customer
5ORDER BY COUNT(*) DESC -- sort customers by total orders (highest first)
6LIMIT 1; -- pick the customer with maximum orders