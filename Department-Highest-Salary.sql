1-- Write your PostgreSQL query statement below
2SELECT d.name AS Department, e.name AS Employee, e.salary -- department, employee, salary
3FROM Employee e
4JOIN Department d ON e.departmentId = d.id -- map employee to department
5WHERE (e.departmentId, e.salary) IN (
6    SELECT departmentId, MAX(salary) -- find max salary per department
7    FROM Employee
8    GROUP BY departmentId
9);