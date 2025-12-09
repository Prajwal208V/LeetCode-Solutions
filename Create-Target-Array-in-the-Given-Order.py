1from typing import List
2
3class Solution:
4    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
5        target = []
6        for i, v in zip(index, nums):
7            target.insert(i, v)
8        return target
9