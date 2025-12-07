1class Solution:
2    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
3        n = len(points)
4        ans = 0
5        for i in range(n):
6            x1, y1 = points[i]
7            cnt = {}
8            for j in range(n):
9                if i == j:
10                    continue
11                x2, y2 = points[j]
12                d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
13                cnt[d] = cnt.get(d, 0) + 1
14            for c in cnt.values():
15                if c > 1:
16                    ans += c * (c - 1)
17        return ans