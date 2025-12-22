1-- Write your PostgreSQL query statement below
2SELECT
3  employee_id,
4  CASE
5    WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
6    ELSE 0
7  END AS bonus
8FROM Employees
9ORDER BY employee_id;