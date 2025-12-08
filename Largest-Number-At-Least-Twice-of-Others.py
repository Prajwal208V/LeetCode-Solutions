1class Solution:
2    def dominantIndex(self, nums: list[int]) -> int:
3        if len(nums) == 1:
4            return 0
5        max1 = max2 = -1
6        idx = -1
7        for i, v in enumerate(nums):
8            if v > max1:
9                max2 = max1
10                max1 = v
11                idx = i
12            elif v > max2:
13                max2 = v
14        return idx if max1 >= 2 * max2 else -1