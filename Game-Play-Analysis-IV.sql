1-- Write your PostgreSQL query statement below
2SELECT ROUND(
3    COUNT(DISTINCT a1.player_id)::decimal / COUNT(DISTINCT a.player_id), 2 -- fraction of returning players
4) AS fraction
5FROM Activity a
6LEFT JOIN Activity a1
7ON a.player_id = a1.player_id -- match same player
8AND a1.event_date = a.event_date + INTERVAL '1 day' -- next day login
9WHERE a.event_date = (
10    SELECT MIN(event_date) -- player's first login date
11    FROM Activity
12    WHERE player_id = a.player_id
13);