1from typing import List
2
3class Solution:
4    def rob(self, nums: List[int]) -> int:
5        if len(nums) == 1:
6            return nums[0]
7
8        def rob_linear(arr: List[int]) -> int:
9            prev2 = 0
10            prev1 = 0
11            for x in arr:
12                cur = max(prev1, prev2 + x)
13                prev2 = prev1
14                prev1 = cur
15            return prev1
16
17        return max(
18            rob_linear(nums[:-1]),
19            rob_linear(nums[1:])
20        )