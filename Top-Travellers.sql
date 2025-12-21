1-- Write your PostgreSQL query statement below
2SELECT u.name, -- user name
3COALESCE(SUM(r.distance), 0) AS travelled_distance -- total travelled distance
4FROM Users u
5LEFT JOIN Rides r ON u.id = r.user_id -- include users with no rides
6GROUP BY u.id, u.name -- group by user
7ORDER BY travelled_distance DESC, u.name ASC; -- sort by distance then name