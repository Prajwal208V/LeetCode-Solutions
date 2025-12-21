1# Write your MySQL query statement below
2SELECT name AS Customers -- select customer name
3FROM Customers
4WHERE id NOT IN (SELECT customerId FROM Orders); -- exclude customers who placed orders