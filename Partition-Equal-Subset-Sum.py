1class Solution:
2    def canPartition(self, nums):
3        total = sum(nums)
4        if total % 2 != 0:
5            return False
6
7        target = total // 2
8        dp = [False] * (target + 1)
9        dp[0] = True
10
11        for num in nums:
12            for s in range(target, num - 1, -1):
13                dp[s] = dp[s] or dp[s - num]
14
15        return dp[target]