1-- Write your PostgreSQL query statement below
2SELECT score, -- display score
3DENSE_RANK() OVER (ORDER BY score DESC) AS rank -- assign rank without gaps for same scores
4FROM Scores
5ORDER BY score DESC; -- final ordering by score descending