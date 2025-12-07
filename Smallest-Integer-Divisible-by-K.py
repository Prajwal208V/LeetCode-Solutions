1class Solution:
2    def smallestRepunitDivByK(self, k: int) -> int:
3        if k % 2 == 0 or k % 5 == 0:
4            return -1
5        rem = 0
6        for i in range(1, k + 1):
7            rem = (rem * 10 + 1) % k
8            if rem == 0:
9                return i
10        return -1