1class Solution:
2    def distinctAverages(self, nums: list[int]) -> int:
3        nums.sort()
4        s = set()
5        l, r = 0, len(nums) - 1
6        while l < r:
7            s.add(nums[l] + nums[r])
8            l += 1
9            r -= 1
10        return len(s)