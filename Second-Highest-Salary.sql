1-- Write your PostgreSQL query statement below
2SELECT MAX(salary) AS SecondHighestSalary -- get second highest salary
3FROM Employee
4WHERE salary < (SELECT MAX(salary) FROM Employee); -- exclude highest salary