1import random
2import bisect
3
4class Solution:
5    def __init__(self, rects):
6        self.rects = rects
7        self.prefix = []
8        total = 0
9
10        for x1, y1, x2, y2 in rects:
11            total += (x2 - x1 + 1) * (y2 - y1 + 1)
12            self.prefix.append(total)
13
14    def pick(self):
15        r = random.randint(1, self.prefix[-1])
16        idx = bisect.bisect_left(self.prefix, r)
17        x1, y1, x2, y2 = self.rects[idx]
18        return [
19            random.randint(x1, x2),
20            random.randint(y1, y2)
21        ]
22
23# Your Solution object will be instantiated and called as such:
24# obj = Solution(rects)
25# param_1 = obj.pick()