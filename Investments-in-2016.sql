1-- Write your PostgreSQL query statement below
2SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016 -- cast sum to numeric before rounding
3FROM Insurance
4WHERE tiv_2015 IN ( -- tiv_2015 must appear more than once
5    SELECT tiv_2015
6    FROM Insurance
7    GROUP BY tiv_2015
8    HAVING COUNT(*) > 1
9)
10AND (lat, lon) IN ( -- location must be unique
11    SELECT lat, lon
12    FROM Insurance
13    GROUP BY lat, lon
14    HAVING COUNT(*) = 1
15);