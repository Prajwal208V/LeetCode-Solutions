1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4        i = 0
5        while i < n:
6            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
7                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
8            else:
9                i += 1
10        for i in range(n):
11            if nums[i] != i + 1:
12                return i + 1
13        return n + 1
14