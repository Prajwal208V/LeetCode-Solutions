# Write your MySQL query statement below
select E.name as Employee from Employee E
where E.managerId in (select M.id from Employee M
                     where E.salary > M.salary)