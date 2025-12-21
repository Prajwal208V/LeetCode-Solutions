1-- Write your PostgreSQL query statement below
2SELECT e1.employee_id, e1.name, -- manager id and name
3COUNT(e2.employee_id) AS reports_count, -- number of direct reports
4ROUND(AVG(e2.age)::numeric, 0) AS average_age -- average age of reports rounded
5FROM Employees e1
6JOIN Employees e2 ON e1.employee_id = e2.reports_to -- self join for reporting structure
7GROUP BY e1.employee_id, e1.name -- group by manager
8ORDER BY e1.employee_id; -- order by employee id