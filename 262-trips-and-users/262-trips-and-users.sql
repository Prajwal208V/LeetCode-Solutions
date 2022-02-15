# Write your MySQL query statement below
with cte as (
    SELECT
        a.request_at,
        a.status
    FROM
        Trips a left join Users b on a.client_id = b.users_id 
                left join Users c on a.driver_id = c.users_id
    WHERE b.banned = 'No' and c.banned = 'No' and request_at between '2013-10-01' and '2013-10-03'
)

SELECT 
    request_at as Day,
    round((sum(case when status = 'completed' then 0 else 1 end)/count(*)),2) as 'Cancellation Rate'
FROM cte
GROUP BY 
    Day