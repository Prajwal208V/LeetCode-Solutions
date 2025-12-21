1CREATE OR REPLACE FUNCTION NthHighestSalary(N INTEGER) -- function name required by LeetCode
2RETURNS INTEGER AS $$ 
3    SELECT (
4        SELECT salary -- pick nth highest salary
5        FROM Employee
6        GROUP BY salary -- remove duplicates
7        ORDER BY salary DESC -- highest to lowest
8        OFFSET GREATEST(N - 1, 0) LIMIT 1 -- prevent negative offset
9    )
10    WHERE N > 0; -- return NULL automatically when N <= 0
11$$ LANGUAGE sql;