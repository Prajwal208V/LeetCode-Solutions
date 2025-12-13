1from typing import List
2
3class Solution:
4    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
5        size = len(primes)
6        dp = [1] * n
7        idx = [0] * size
8        vals = primes[:]
9
10        for i in range(1, n):
11            next_val = min(vals)
12            dp[i] = next_val
13
14            for j in range(size):
15                if vals[j] == next_val:
16                    idx[j] += 1
17                    vals[j] = dp[idx[j]] * primes[j]
18
19        return dp[-1]
20