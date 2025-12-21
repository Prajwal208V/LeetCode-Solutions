1# Write your MySQL query statement below
2UPDATE Salary
3SET sex = CASE 
4    WHEN sex = 'm' THEN 'f' -- convert male to female
5    WHEN sex = 'f' THEN 'm' -- convert female to male
6END;