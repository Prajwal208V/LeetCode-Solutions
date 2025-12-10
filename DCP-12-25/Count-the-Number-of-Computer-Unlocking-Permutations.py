1from typing import List
2
3class Solution:
4    def countPermutations(self, complexity: List[int]) -> int:
5        MOD = 10**9 + 7
6        n = len(complexity)
7        for i in range(1, n):
8            if complexity[i] <= complexity[0]:
9                return 0
10        ans = 1
11        for i in range(1, n):
12            ans = ans * i % MOD
13        return ans
14