1from typing import List
2
3class Solution:
4    def removeDuplicates(self, nums: List[int]) -> int:
5        if len(nums) <= 2:
6            return len(nums)
7
8        i = 2
9        for j in range(2, len(nums)):
10            if nums[j] != nums[i - 2]:
11                nums[i] = nums[j]
12                i += 1
13
14        return i