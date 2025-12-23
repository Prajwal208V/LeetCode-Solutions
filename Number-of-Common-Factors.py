1class Solution:
2    def commonFactors(self, a: int, b: int) -> int:
3        res = 0
4        for i in range(1, min(a, b) + 1):
5            if a % i == 0 and b % i == 0:
6                res += 1
7        return res