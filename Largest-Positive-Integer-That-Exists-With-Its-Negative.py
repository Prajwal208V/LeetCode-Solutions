1class Solution:
2    def findMaxK(self, nums: list[int]) -> int:
3        s = set(nums)
4        ans = -1
5        for x in s:
6            if x > 0 and -x in s:
7                ans = max(ans, x)
8        return ans