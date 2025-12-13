1class Solution:
2    def getMoneyAmount(self, n: int) -> int:
3        dp = [[0] * (n + 1) for _ in range(n + 1)]
4
5        for length in range(2, n + 1):
6            for start in range(1, n - length + 2):
7                end = start + length - 1
8                dp[start][end] = float('inf')
9                for x in range(start, end + 1):
10                    cost = x + max(
11                        dp[start][x - 1] if x - 1 >= start else 0,
12                        dp[x + 1][end] if x + 1 <= end else 0
13                    )
14                    dp[start][end] = min(dp[start][end], cost)
15
16        return dp[1][n]