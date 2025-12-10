1from typing import List
2
3class Solution:
4    def finalPrices(self, prices: List[int]) -> List[int]:
5        stack = []
6        for i, p in enumerate(prices):
7            while stack and prices[stack[-1]] >= p:
8                j = stack.pop()
9                prices[j] -= p
10            stack.append(i)
11        return prices
12