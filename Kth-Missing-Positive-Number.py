1from typing import List
2
3class Solution:
4    def findKthPositive(self, arr: List[int], k: int) -> int:
5        lo, hi = 0, len(arr)
6        while lo < hi:
7            mid = (lo + hi) // 2
8            missing = arr[mid] - (mid + 1)
9            if missing < k:
10                lo = mid + 1
11            else:
12                hi = mid
13        return lo + k