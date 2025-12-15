1from typing import List
2
3class Solution:
4    def maxProductDifference(self, nums: List[int]) -> int:
5        nums.sort()
6        return nums[-1] * nums[-2] - nums[0] * nums[1]