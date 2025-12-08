1class Solution:
2    def minCostClimbingStairs(self, cost: list[int]) -> int:
3        n = len(cost)
4        prev2, prev1 = 0, 0
5        for i in range(2, n + 1):
6            cur = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
7            prev2, prev1 = prev1, cur
8        return prev1
9