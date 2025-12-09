1from typing import List
2
3class Solution:
4    def getNoZeroIntegers(self, n: int) -> List[int]:
5        def has_zero(x: int) -> bool:
6            return '0' in str(x)
7        for a in range(1, n):
8            b = n - a
9            if not has_zero(a) and not has_zero(b):
10                return [a, b]
11