1# Write your MySQL query statement below
2SELECT DISTINCT
3    author_id AS id
4FROM Views
5WHERE author_id = viewer_id
6ORDER BY id;
7