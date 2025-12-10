1from typing import List
2
3class Solution:
4    def runningSum(self, nums: List[int]) -> List[int]:
5        s = 0
6        res = []
7        for x in nums:
8            s += x
9            res.append(s)
10        return res
11