1-- Write your PostgreSQL query statement below
2SELECT employee_id, department_id -- select employee and department
3FROM Employee
4WHERE primary_flag = 'Y' -- pick primary department
5   OR employee_id NOT IN ( -- employees without any primary department
6       SELECT employee_id
7       FROM Employee
8       WHERE primary_flag = 'Y'
9   );