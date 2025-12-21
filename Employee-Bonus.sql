1# Write your MySQL query statement below
2SELECT e.name, b.bonus -- select employee name and bonus
3FROM Employee e
4LEFT JOIN Bonus b ON e.empId = b.empId -- include employees even if bonus is missing
5WHERE b.bonus < 1000 OR b.bonus IS NULL; -- filter low bonus or no bonus