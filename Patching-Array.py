1class Solution:
2    def minPatches(self, nums: List[int], n: int) -> int:
3        miss = 1
4        i = 0
5        patches = 0
6        while miss <= n:
7            if i < len(nums) and nums[i] <= miss:
8                miss += nums[i]
9                i += 1
10            else:
11                miss += miss
12                patches += 1
13        return patches