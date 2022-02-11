# Write your MySQL query statement below
WITH temp AS
(SELECT
    id,
    visit_date,
    people,
    ROW_NUMBER() OVER (ORDER BY id) AS my_rank
FROM 
    Stadium
WHERE 
    people >= 100)
    
SELECT
    id,
    visit_date,
    people
FROM 
    temp
WHERE id-my_rank IN (SELECT id-my_rank FROM temp
GROUP BY id-my_rank
HAVING COUNT(*) >=3)