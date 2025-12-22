1-- Write your PostgreSQL query statement below
2SELECT
3  user_id,
4  MAX(time_stamp) AS last_stamp
5FROM
6  Logins
7WHERE
8  EXTRACT(YEAR FROM time_stamp) = 2020
9GROUP BY
10  user_id;