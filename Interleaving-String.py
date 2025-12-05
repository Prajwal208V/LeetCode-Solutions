1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m, n = len(s1), len(s2)
4        if m + n != len(s3):
5            return False
6        dp = [False] * (n + 1)
7        dp[0] = True
8        for j in range(1, n + 1):
9            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
10        for i in range(1, m + 1):
11            dp[0] = dp[0] and s1[i-1] == s3[i-1]
12            for j in range(1, n + 1):
13                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
14        return dp[n]
15