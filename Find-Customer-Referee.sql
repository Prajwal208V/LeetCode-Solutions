1# Write your MySQL query statement below
2SELECT name -- select customer name
3FROM Customer
4WHERE referee_id != 2 OR referee_id IS NULL; -- exclude customers referred by id 2