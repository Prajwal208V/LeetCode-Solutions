1class Solution:
2    def countDigitOne(self, n: int) -> int:
3        res = 0
4        factor = 1
5        while factor <= n:
6            lower = n % factor
7            cur = (n // factor) % 10
8            higher = n // (factor * 10)
9
10            if cur == 0:
11                res += higher * factor
12            elif cur == 1:
13                res += higher * factor + lower + 1
14            else:
15                res += (higher + 1) * factor
16
17            factor *= 10
18        return res
19