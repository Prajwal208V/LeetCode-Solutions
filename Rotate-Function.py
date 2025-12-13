1from typing import List
2
3class Solution:
4    def maxRotateFunction(self, nums: List[int]) -> int:
5        n = len(nums)
6        total_sum = sum(nums)
7
8        f = sum(i * nums[i] for i in range(n))
9        res = f
10
11        for i in range(1, n):
12            f = f + total_sum - n * nums[n - i]
13            res = max(res, f)
14
15        return res