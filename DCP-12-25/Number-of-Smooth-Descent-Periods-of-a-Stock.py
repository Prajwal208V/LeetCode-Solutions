1from typing import List
2
3class Solution:
4    def getDescentPeriods(self, prices: List[int]) -> int:
5        total = 1
6        curr = 1
7        
8        for i in range(1, len(prices)):
9            if prices[i] == prices[i - 1] - 1:
10                curr += 1
11            else:
12                curr = 1
13            total += curr
14        
15        return total