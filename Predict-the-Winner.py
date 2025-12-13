1class Solution:
2    def predictTheWinner(self, nums):
3        from functools import lru_cache
4
5        @lru_cache(None)
6        def dfs(l, r):
7            if l == r:
8                return nums[l]
9            return max(
10                nums[l] - dfs(l + 1, r),
11                nums[r] - dfs(l, r - 1)
12            )
13
14        return dfs(0, len(nums) - 1) >= 0