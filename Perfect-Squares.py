1class Solution:
2    def numSquares(self, n: int) -> int:
3        dp = [float('inf')]*(n+1)
4        dp[0]=0
5        for i in range(1,n+1):
6            j=1
7            while j*j <= i:
8                dp[i] = min(dp[i],dp[i-j*j]+1)
9                j+=1
10        return dp[n]
11
12        