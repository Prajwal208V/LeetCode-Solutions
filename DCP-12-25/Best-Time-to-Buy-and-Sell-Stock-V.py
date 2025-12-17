1from typing import List
2
3class Solution:
4    def maximumProfit(self, prices: List[int], k: int) -> int:
5        n = len(prices)
6        # dp[i][j][0]: max profit up to day i with j transactions and no position
7        # dp[i][j][1]: holding a long position
8        # dp[i][j][2]: holding a short position
9        dp = [[[0]*3 for _ in range(k+1)] for _ in range(n)]
10        
11        # initialize base states
12        for j in range(1, k+1):
13            dp[0][j][1] = -prices[0]  # bought stock
14            dp[0][j][2] = prices[0]   # shorted stock
15        
16        for i in range(1, n):
17            for j in range(1, k+1):
18                dp[i][j][0] = max(
19                    dp[i-1][j][0],
20                    dp[i-1][j][1] + prices[i],
21                    dp[i-1][j][2] - prices[i]
22                )
23                dp[i][j][1] = max(
24                    dp[i-1][j][1],
25                    dp[i-1][j-1][0] - prices[i]
26                )
27                dp[i][j][2] = max(
28                    dp[i-1][j][2],
29                    dp[i-1][j-1][0] + prices[i]
30                )
31        
32        return dp[n-1][k][0]