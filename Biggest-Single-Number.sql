1# Write your MySQL query statement below
2SELECT MAX(num) AS num -- select largest unique number
3FROM MyNumbers
4WHERE num IN (
5    SELECT num -- find numbers appearing only once
6    FROM MyNumbers
7    GROUP BY num
8    HAVING COUNT(num) = 1
9);