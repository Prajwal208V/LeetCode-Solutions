1-- Write your PostgreSQL query statement below
2SELECT u.unique_id, e.name -- show unique id and employee name
3FROM Employees e
4LEFT JOIN EmployeeUNI u
5ON e.id = u.id; -- map employee id to unique id