1# Write your MySQL query statement below
2SELECT
3    activity_date AS day,
4    COUNT(DISTINCT user_id) AS active_users
5FROM Activity
6WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
7GROUP BY activity_date
8ORDER BY activity_date;
9