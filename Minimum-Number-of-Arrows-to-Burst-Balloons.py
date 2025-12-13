1class Solution:
2    def findMinArrowShots(self, points):
3        if not points:
4            return 0
5
6        points.sort(key=lambda x: x[1])
7
8        arrows = 1
9        end = points[0][1]
10
11        for start, finish in points[1:]:
12            if start > end:
13                arrows += 1
14                end = finish
15
16        return arrows