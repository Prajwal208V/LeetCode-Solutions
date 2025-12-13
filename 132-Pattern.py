1class Solution:
2    def find132pattern(self, nums):
3        stack = []
4        third = float("-inf")
5
6        for i in range(len(nums) - 1, -1, -1):
7            if nums[i] < third:
8                return True
9
10            while stack and nums[i] > stack[-1]:
11                third = stack.pop()
12
13            stack.append(nums[i])
14
15        return False