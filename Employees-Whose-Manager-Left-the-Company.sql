1-- Write your PostgreSQL query statement below
2SELECT employee_id
3FROM Employees
4WHERE salary < 30000
5  AND manager_id IS NOT NULL
6  AND manager_id NOT IN (SELECT employee_id FROM Employees)
7ORDER BY employee_id;