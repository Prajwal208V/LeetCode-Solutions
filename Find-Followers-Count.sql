1-- Write your PostgreSQL query statement below
2SELECT user_id, -- user being followed
3COUNT(follower_id) AS followers_count -- total followers
4FROM Followers
5GROUP BY user_id -- group per user
6ORDER BY user_id; -- order by user id