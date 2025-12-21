1# Write your MySQL query statement below
2SELECT name -- select salesperson name
3FROM SalesPerson
4WHERE sales_id NOT IN (
5    SELECT o.sales_id -- salespeople involved in red company orders
6    FROM Orders o
7    JOIN Company c ON o.com_id = c.com_id -- link orders with companies
8    WHERE c.name = 'RED' -- filter company named RED
9);