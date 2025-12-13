1class Solution:
2    def minMoves2(self, nums):
3        nums.sort()
4        median = nums[len(nums) // 2]
5        return sum(abs(num - median) for num in nums)   