1from typing import List
2
3class Solution:
4    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
5        x1, y1 = coordinates[0]
6        x2, y2 = coordinates[1]
7        
8        dx = x2 - x1
9        dy = y2 - y1
10        
11        for x, y in coordinates[2:]:
12            if dy * (x - x1) != dx * (y - y1):
13                return False
14        return True