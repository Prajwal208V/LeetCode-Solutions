1from collections import defaultdict
2
3class Solution:
4    def countLargestGroup(self, n: int) -> int:
5        groups = defaultdict(int)
6        for x in range(1, n + 1):
7            s = 0
8            y = x
9            while y:
10                s += y % 10
11                y //= 10
12            groups[s] += 1
13        max_size = max(groups.values())
14        return sum(1 for v in groups.values() if v == max_size)
15