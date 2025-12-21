1-- Write your PostgreSQL query statement below
2SELECT sell_date, -- sale date
3COUNT(DISTINCT product) AS num_sold, -- count unique products sold
4STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products -- concatenate products in alphabetical order
5FROM Activities
6GROUP BY sell_date -- group by date
7ORDER BY sell_date; -- order by date