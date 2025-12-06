1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [1] * n
4        for _ in range(1, m):
5            for j in range(1, n):
6                dp[j] += dp[j-1]
7        return dp[-1]