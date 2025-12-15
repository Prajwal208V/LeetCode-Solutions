1from typing import List
2
3class Solution:
4    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
5        return min(abs(i - start) for i, v in enumerate(nums) if v == target)