1from typing import List
2
3class Solution:
4    def combinationSum4(self, nums: List[int], target: int) -> int:
5        dp = [0] * (target + 1)
6        dp[0] = 1
7
8        for i in range(1, target + 1):
9            for num in nums:
10                if i >= num:
11                    dp[i] += dp[i - num]
12
13        return dp[target]