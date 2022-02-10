# Write your MySQL query statement below
 select b.name Department, a.name Employee, a.salary
from
   (select name, departmentId, DENSE_RANK() OVER(partition by departmentId order by salary desc) as rak, salary
    from Employee) a join Department b on a.departmentId = b.id
where rak in (1, 2, 3)