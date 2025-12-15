1from typing import List
2
3class Solution:
4    def maxAscendingSum(self, nums: List[int]) -> int:
5        curr = ans = nums[0]
6        
7        for i in range(1, len(nums)):
8            if nums[i] > nums[i - 1]:
9                curr += nums[i]
10            else:
11                curr = nums[i]
12            ans = max(ans, curr)
13        
14        return ans