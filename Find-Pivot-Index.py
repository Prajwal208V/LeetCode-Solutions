1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        total = sum(nums)
4        left = 0
5        for i, x in enumerate(nums):
6            if left == total - left - x:
7                return i
8            left += x
9        return -1