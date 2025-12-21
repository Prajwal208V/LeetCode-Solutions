1# Write your MySQL query statement below
2SELECT x, y, z, -- select all sides
3CASE 
4    WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes' -- triangle condition
5    ELSE 'No' -- not a triangle
6END AS triangle
7FROM Triangle;