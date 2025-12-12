1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        maxprofit = 0
4        minSoFar = prices[0]
5        for val in prices:
6            minSoFar = min(val,minSoFar)
7            profit = val - minSoFar
8            maxprofit = max(profit,maxprofit)
9        
10        return maxprofit