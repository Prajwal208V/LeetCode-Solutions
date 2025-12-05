1from math import isqrt
2
3class Solution:
4    def pivotInteger(self, n: int) -> int:
5        t = n * (n + 1) // 2
6        s = isqrt(t)
7        return s if s * s == t else -1
8