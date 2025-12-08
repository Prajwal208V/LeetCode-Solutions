1class Solution:
2    def largestTriangleArea(self, points: List[List[int]]) -> float:
3        def area(p1, p2, p3):
4            # Shoelace formula for triangle area
5            x1, y1 = p1
6            x2, y2 = p2
7            x3, y3 = p3
8            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
9        
10        max_area = 0
11        n = len(points)
12        
13        # Try all combinations of 3 points
14        for i in range(n):
15            for j in range(i + 1, n):
16                for k in range(j + 1, n):
17                    max_area = max(max_area, area(points[i], points[j], points[k]))
18        
19        return max_area