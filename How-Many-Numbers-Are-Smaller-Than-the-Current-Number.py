1from typing import List
2
3class Solution:
4    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
5        sorted_nums = sorted(nums)
6        rank = {}
7        for i, v in enumerate(sorted_nums):
8            if v not in rank:
9                rank[v] = i
10        return [rank[v] for v in nums]
11