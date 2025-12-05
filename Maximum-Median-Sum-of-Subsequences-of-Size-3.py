1class Solution:
2    def maximumMedianSum(self, nums):
3        nums.sort(reverse=True)
4        n = len(nums)
5        k = n // 3
6        median_sum = 0
7        for i in range(1, 2 * k, 2):
8            median_sum += nums[i]
9        return median_sum