1-- Write your PostgreSQL query statement below
2SELECT event_day AS day, emp_id, -- date and employee id
3SUM(out_time - in_time) AS total_time -- total working time per day
4FROM Employees
5GROUP BY event_day, emp_id; -- group by date and employee