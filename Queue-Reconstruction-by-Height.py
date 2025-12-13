1from typing import List
2
3class Solution:
4    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
5        people.sort(key=lambda x: (-x[0], x[1]))
6        res = []
7        for p in people:
8            res.insert(p[1], p)
9        return res