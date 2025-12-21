1# Write your MySQL query statement below
2SELECT player_id, MIN(event_date) AS first_login -- earliest login per player
3FROM Activity
4GROUP BY player_id; -- group by player