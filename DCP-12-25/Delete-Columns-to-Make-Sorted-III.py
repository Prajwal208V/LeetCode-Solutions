1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        m, n = len(strs), len(strs[0])
4        dp = [1] * n
5        for j in range(n):
6            for i in range(j):
7                if all(strs[row][i] <= strs[row][j] for row in range(m)):
8                    dp[j] = max(dp[j], dp[i] + 1)
9        return n - max(dp)