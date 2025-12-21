1-- Write your PostgreSQL query statement below
2SELECT DISTINCT l1.num AS ConsecutiveNums -- select number appearing consecutively
3FROM Logs l1
4JOIN Logs l2 ON l1.id = l2.id - 1 -- join next row
5JOIN Logs l3 ON l2.id = l3.id - 1 -- join third consecutive row
6WHERE l1.num = l2.num AND l2.num = l3.num; -- all three values must match