1class Solution:
2    def totalHammingDistance(self, nums):
3        res = 0
4        n = len(nums)
5
6        for bit in range(32):
7            ones = 0
8            for num in nums:
9                ones += (num >> bit) & 1
10            res += ones * (n - ones)
11
12        return res