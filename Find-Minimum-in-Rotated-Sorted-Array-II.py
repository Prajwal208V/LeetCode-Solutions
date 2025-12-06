1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4        while l < r:
5            m = (l + r) // 2
6            if nums[m] > nums[r]:
7                l = m + 1
8            elif nums[m] < nums[r]:
9                r = m
10            else:
11                r -= 1
12        return nums[l]
13