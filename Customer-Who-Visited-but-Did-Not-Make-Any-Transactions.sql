1-- Write your PostgreSQL query statement below
2SELECT v.customer_id, -- customer id
3COUNT(*) AS count_no_trans -- count visits without transactions
4FROM Visits v
5LEFT JOIN Transactions t ON v.visit_id = t.visit_id -- join visits with transactions
6WHERE t.transaction_id IS NULL -- keep visits with no transaction
7GROUP BY v.customer_id; -- group by customer