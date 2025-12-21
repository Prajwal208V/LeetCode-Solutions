1# Write your MySQL query statement below
2SELECT w1.id -- select current day id
3FROM Weather w1
4JOIN Weather w2
5ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 -- previous day comparison
6AND w1.temperature > w2.temperature; -- rising temperature condition