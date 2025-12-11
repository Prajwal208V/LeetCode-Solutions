1from typing import List
2
3class Solution:
4    def removeDuplicates(self, nums: List[int]) -> int:
5        if not nums:
6            return 0
7        i = 1
8        for j in range(1, len(nums)):
9            if nums[j] != nums[j - 1]:
10                nums[i] = nums[j]
11                i += 1
12        return i    