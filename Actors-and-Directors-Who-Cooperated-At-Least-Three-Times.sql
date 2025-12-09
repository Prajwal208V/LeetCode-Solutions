1# Write your MySQL query statement below
2SELECT
3    actor_id,
4    director_id
5FROM
6    ActorDirector
7GROUP BY
8    actor_id,
9    director_id
10HAVING
11    COUNT(*) >= 3;
12