1from typing import List
2
3class Solution:
4    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
5        count = [0, 0]
6        for s in students:
7            count[s] += 1
8        
9        for sand in sandwiches:
10            if count[sand] == 0:
11                break
12            count[sand] -= 1
13        
14        return count[0] + count[1]