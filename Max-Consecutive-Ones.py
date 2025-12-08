1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3        best = cur = 0
4        for x in nums:
5            if x == 1:
6                cur += 1
7                if cur > best:
8                    best = cur
9            else:
10                cur = 0
11        return best