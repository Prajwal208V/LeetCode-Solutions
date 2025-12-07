1class Solution:
2    def maxSumDivThree(self, nums: list[int]) -> int:
3        dp = [0, float('-inf'), float('-inf')]
4        for x in nums:
5            cur = dp[:]
6            for r in range(3):
7                dp[(r + x) % 3] = max(dp[(r + x) % 3], cur[r] + x)
8        return dp[0]