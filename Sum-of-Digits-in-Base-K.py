1class Solution:
2    def sumBase(self, n: int, k: int) -> int:
3        total = 0
4        while n > 0:
5            total += n % k
6            n //= k
7        return total