1from typing import List
2
3class Solution:
4    def sumZero(self, n: int) -> List[int]:
5        res = []
6        for i in range(1, n // 2 + 1):
7            res.append(i)
8            res.append(-i)
9        if n % 2 == 1:
10            res.append(0)
11        return res
12