1-- Write your PostgreSQL query statement below
2SELECT a.machine_id, -- machine id
3ROUND(AVG(b.timestamp - a.timestamp)::numeric, 3) AS processing_time -- average processing time
4FROM Activity a
5JOIN Activity b
6ON a.machine_id = b.machine_id -- same machine
7AND a.process_id = b.process_id -- same process
8AND a.activity_type = 'start' -- start time
9AND b.activity_type = 'end' -- end time
10GROUP BY a.machine_id; -- group by machine