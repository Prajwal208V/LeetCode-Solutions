1class Solution:
2    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
3        left = 0
4        total = 0
5        ans = float('inf')
6        for right in range(len(nums)):
7            total += nums[right]
8            while total >= target:
9                ans = min(ans, right - left + 1)
10                total -= nums[left]
11                left += 1
12        return 0 if ans == float('inf') else ans