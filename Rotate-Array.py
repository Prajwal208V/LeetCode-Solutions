1from typing import List
2
3class Solution:
4    def rotate(self, nums: List[int], k: int) -> None:
5        k %= len(nums)
6
7        def rev(l, r):
8            while l < r:
9                nums[l], nums[r] = nums[r], nums[l]
10                l += 1
11                r -= 1
12
13        rev(0, len(nums) - 1)
14        rev(0, k - 1)
15        rev(k, len(nums) - 1)
16