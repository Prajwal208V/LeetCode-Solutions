1from typing import List
2
3class Solution:
4    def findNumbers(self, nums: List[int]) -> int:
5        res = 0
6        for x in nums:
7            if len(str(x)) % 2 == 0:
8                res += 1
9        return res
10