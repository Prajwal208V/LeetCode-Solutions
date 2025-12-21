1-- Write your PostgreSQL query statement below
2SELECT p.product_id, p.product_name -- select product details
3FROM Product p
4JOIN Sales s ON p.product_id = s.product_id -- join sales with product
5GROUP BY p.product_id, p.product_name -- group by product
6HAVING MIN(s.sale_date) >= DATE '2019-01-01' -- first sale on or after Jan 1, 2019
7AND MAX(s.sale_date) <= DATE '2019-03-31'; -- last sale on or before Mar 31, 2019