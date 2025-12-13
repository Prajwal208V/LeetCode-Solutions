1from typing import List
2
3class Solution:
4    def coinChange(self, coins: List[int], amount: int) -> int:
5        dp = [amount + 1] * (amount + 1)
6        dp[0] = 0
7
8        for i in range(1, amount + 1):
9            for c in coins:
10                if i >= c:
11                    dp[i] = min(dp[i], dp[i - c] + 1)
12
13        return dp[amount] if dp[amount] != amount + 1 else -1
14