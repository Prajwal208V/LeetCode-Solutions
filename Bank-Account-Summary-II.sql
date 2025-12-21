1-- Write your PostgreSQL query statement below
2SELECT u.name, -- user name
3SUM(t.amount) AS balance -- total balance per user
4FROM Users u
5JOIN Transactions t ON u.account = t.account -- join users with transactions
6GROUP BY u.name -- group by user
7HAVING SUM(t.amount) > 10000; -- only users with balance greater than 10000