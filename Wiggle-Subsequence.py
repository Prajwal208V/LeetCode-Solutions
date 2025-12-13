1from typing import List
2
3class Solution:
4    def wiggleMaxLength(self, nums: List[int]) -> int:
5        if len(nums) < 2:
6            return len(nums)
7
8        up = 1
9        down = 1
10
11        for i in range(1, len(nums)):
12            if nums[i] > nums[i - 1]:
13                up = down + 1
14            elif nums[i] < nums[i - 1]:
15                down = up + 1
16
17        return max(up, down)  