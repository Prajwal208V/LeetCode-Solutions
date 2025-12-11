1from typing import List
2
3class Solution:
4    def removeElement(self, nums: List[int], val: int) -> int:
5        i = 0
6        for j in range(len(nums)):
7            if nums[j] != val:
8                nums[i] = nums[j]
9                i += 1
10        return i