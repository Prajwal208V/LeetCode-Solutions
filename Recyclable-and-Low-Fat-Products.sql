1-- Write your PostgreSQL query statement below
2SELECT product_id -- select product id
3FROM Products
4WHERE low_fats = 'Y' AND recyclable = 'Y'; -- must satisfy both conditions