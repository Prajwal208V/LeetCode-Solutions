1-- Write your PostgreSQL query statement below
2SELECT user_id, -- user id
3UPPER(LEFT(name, 1)) || LOWER(SUBSTRING(name FROM 2)) AS name -- capitalize first letter and lowercase rest
4FROM Users
5ORDER BY user_id; -- order by user id