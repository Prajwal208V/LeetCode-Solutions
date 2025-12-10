1from typing import List
2
3class Solution:
4    def isBoomerang(self, points: List[List[int]]) -> bool:
5        (x1, y1), (x2, y2), (x3, y3) = points
6        if [x1, y1] == [x2, y2] or [x1, y1] == [x3, y3] or [x2, y2] == [x3, y3]:
7            return False
8        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
9