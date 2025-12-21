1-- Write your PostgreSQL query statement below
2SELECT user_id, name, mail -- select required output columns
3FROM Users
4WHERE mail ~ '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'; -- valid leetcode email format