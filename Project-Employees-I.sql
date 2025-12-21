1-- Write your PostgreSQL query statement below
2SELECT p.project_id, -- select project id
3ROUND(AVG(e.experience_years)::numeric, 2) AS average_years -- average experience rounded to 2 decimals
4FROM Project p
5JOIN Employee e ON p.employee_id = e.employee_id -- join project with employee
6GROUP BY p.project_id; -- group by project