1from typing import List
2
3class Solution:
4    def canBeIncreasing(self, nums: List[int]) -> bool:
5        removed = False
6        for i in range(1, len(nums)):
7            if nums[i] <= nums[i - 1]:
8                if removed:
9                    return False
10                removed = True
11                if i > 1 and nums[i] <= nums[i - 2]:
12                    nums[i] = nums[i - 1]
13        return True