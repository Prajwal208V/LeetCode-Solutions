1from typing import List
2
3class Solution:
4    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
5        if len(nums) < 3:
6            return 0
7
8        curr = 0
9        total = 0
10
11        for i in range(2, len(nums)):
12            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
13                curr += 1
14                total += curr
15            else:
16                curr = 0
17
18        return total