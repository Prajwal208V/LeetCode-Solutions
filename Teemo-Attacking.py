1from typing import List
2
3class Solution:
4    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
5        if not timeSeries:
6            return 0
7        total = 0
8        for i in range(1, len(timeSeries)):
9            total += min(duration, timeSeries[i] - timeSeries[i - 1])
10        return total + duration
11