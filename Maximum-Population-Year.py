1from typing import List
2
3class Solution:
4    def maximumPopulation(self, logs: List[List[int]]) -> int:
5        delta = [0] * 101
6        for b, d in logs:
7            delta[b - 1950] += 1
8            delta[d - 1950] -= 1
9        
10        max_pop = year = curr = 0
11        for i in range(101):
12            curr += delta[i]
13            if curr > max_pop:
14                max_pop = curr
15                year = 1950 + i
16        return year