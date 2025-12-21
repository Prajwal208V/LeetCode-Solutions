1-- Write your PostgreSQL query statement below
2SELECT r.contest_id, -- contest id
3ROUND(
4    100.0 * COUNT(DISTINCT r.user_id) / (SELECT COUNT(*) FROM Users),
5    2
6) AS percentage -- percentage of users attended
7FROM Register r
8GROUP BY r.contest_id -- group by contest
9ORDER BY percentage DESC, r.contest_id ASC; -- sort as required