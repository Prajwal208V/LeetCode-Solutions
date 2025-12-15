1from typing import List
2
3class Solution:
4    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
5        min_dist = float('inf')
6        idx = -1
7        
8        for i, (px, py) in enumerate(points):
9            if px == x or py == y:
10                dist = abs(px - x) + abs(py - y)
11                if dist < min_dist:
12                    min_dist = dist
13                    idx = i
14        
15        return idx