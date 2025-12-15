1from typing import List
2
3class Solution:
4    def minimumDifference(self, nums: List[int], k: int) -> int:
5        nums.sort()
6        ans = float('inf')
7        for i in range(len(nums) - k + 1):
8            ans = min(ans, nums[i + k - 1] - nums[i])
9        return ans