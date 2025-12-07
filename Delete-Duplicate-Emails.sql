1# Write your MySQL query statement below
2DELETE p1
3FROM Person p1
4JOIN Person p2
5ON p1.Email = p2.Email AND p1.Id > p2.Id;
6