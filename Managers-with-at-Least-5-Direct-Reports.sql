1-- Write your PostgreSQL query statement below
2SELECT e.name -- select manager name
3FROM Employee e
4JOIN Employee r ON e.id = r.managerId -- join managers with direct reports
5GROUP BY e.id, e.name -- group by manager
6HAVING COUNT(r.id) >= 5; -- at least 5 direct reports