1class Solution:
2    def subtractProductAndSum(self, n: int) -> int:
3        s = 0
4        p = 1
5        while n > 0:
6            d = n % 10
7            s += d
8            p *= d
9            n //= 10
10        return p - s
11