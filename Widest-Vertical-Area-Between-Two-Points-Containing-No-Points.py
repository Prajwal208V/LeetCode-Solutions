1from typing import List
2
3class Solution:
4    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
5        xs = sorted(point[0] for point in points)
6        max_width = 0
7        for i in range(1, len(xs)):
8            max_width = max(max_width, xs[i] - xs[i - 1])
9        return max_width