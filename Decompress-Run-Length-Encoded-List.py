1from typing import List
2
3class Solution:
4    def decompressRLElist(self, nums: List[int]) -> List[int]:
5        res = []
6        for i in range(0, len(nums), 2):
7            freq = nums[i]
8            val = nums[i + 1]
9            res.extend([val] * freq)
10        return res
11