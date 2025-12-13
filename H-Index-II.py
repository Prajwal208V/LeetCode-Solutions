1from typing import List
2
3class Solution:
4    def hIndex(self, citations: List[int]) -> int:
5        n = len(citations)
6        left, right = 0, n - 1
7
8        while left <= right:
9            mid = (left + right) // 2
10            if citations[mid] >= n - mid:
11                right = mid - 1
12            else:
13                left = mid + 1
14
15        return n - left