1from typing import List
2
3class Solution:
4    def maximumProduct(self, nums: List[int]) -> int:
5        nums.sort()
6        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
7