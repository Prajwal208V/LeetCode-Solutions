1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        n, m = len(s), len(t)
4        if m > n:
5            return 0
6        dp = [0] * (m + 1)
7        dp[0] = 1
8        for i in range(n):
9            for j in range(m, 0, -1):
10                if s[i] == t[j-1]:
11                    dp[j] += dp[j-1]
12        return dp[m]
13   