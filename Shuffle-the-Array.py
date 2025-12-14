1from typing import List
2
3class Solution:
4    def shuffle(self, nums: List[int], n: int) -> List[int]:
5        result = []
6        for i in range(n):
7            result.append(nums[i])
8            result.append(nums[i + n])
9        return result