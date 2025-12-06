1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        for f in (2, 3, 5):
6            while n % f == 0:
7                n //= f
8        return n == 1