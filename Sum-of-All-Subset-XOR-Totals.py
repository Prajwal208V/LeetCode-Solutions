1from typing import List
2
3class Solution:
4    def subsetXORSum(self, nums: List[int]) -> int:
5        res = 0
6        for n in nums:
7            res |= n
8        return res * (1 << (len(nums) - 1))