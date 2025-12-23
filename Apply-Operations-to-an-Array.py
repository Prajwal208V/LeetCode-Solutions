1class Solution:
2    def applyOperations(self, nums: list[int]) -> list[int]:
3        n = len(nums)
4        for i in range(n - 1):
5            if nums[i] == nums[i + 1]:
6                nums[i] *= 2
7                nums[i + 1] = 0
8        res = [x for x in nums if x != 0]
9        return res + [0] * (n - len(res))