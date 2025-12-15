1from typing import List
2
3class Solution:
4    def minOperations(self, nums: List[int]) -> int:
5        ops = 0
6        for i in range(1, len(nums)):
7            if nums[i] <= nums[i - 1]:
8                inc = nums[i - 1] + 1 - nums[i]
9                ops += inc
10                nums[i] += inc
11        return ops 