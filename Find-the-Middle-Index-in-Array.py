1from typing import List
2
3class Solution:
4    def findMiddleIndex(self, nums: List[int]) -> int:
5        total = sum(nums)
6        left = 0
7        for i, v in enumerate(nums):
8            if left == total - left - v:
9                return i
10            left += v
11        return -1