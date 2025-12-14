1from typing import List
2
3class Solution:
4    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
5        max_side = 0
6        count = 0
7        
8        for l, w in rectangles:
9            side = min(l, w)
10            if side > max_side:
11                max_side = side
12                count = 1
13            elif side == max_side:
14                count += 1
15        
16        return count