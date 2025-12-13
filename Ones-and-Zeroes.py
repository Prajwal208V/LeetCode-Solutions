1class Solution:
2    def findMaxForm(self, strs, m, n):
3        dp = [[0] * (n + 1) for _ in range(m + 1)]
4
5        for s in strs:
6            zeros = s.count('0')
7            ones = s.count('1')
8
9            for i in range(m, zeros - 1, -1):
10                for j in range(n, ones - 1, -1):
11                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
12
13        return dp[m][n]