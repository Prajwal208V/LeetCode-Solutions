1import bisect
2
3class Solution:
4    def findRadius(self, houses, heaters):
5        houses.sort()
6        heaters.sort()
7        res = 0
8
9        for house in houses:
10            idx = bisect.bisect_left(heaters, house)
11
12            left = house - heaters[idx - 1] if idx > 0 else float('inf')
13            right = heaters[idx] - house if idx < len(heaters) else float('inf')
14
15            res = max(res, min(left, right))
16
17        return res