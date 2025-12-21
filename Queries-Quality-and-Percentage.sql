1-- Write your PostgreSQL query statement below
2SELECT query_name, -- group by query name
3ROUND(AVG(rating::decimal / position), 2) AS quality, -- average quality score
4ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage -- percentage of poor queries
5FROM Queries
6GROUP BY query_name; -- aggregate per query