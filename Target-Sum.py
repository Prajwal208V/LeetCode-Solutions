1class Solution:
2    def findTargetSumWays(self, nums, target):
3        from functools import lru_cache
4        
5        n = len(nums)
6        
7        @lru_cache(None)
8        def dfs(i, total):
9            if i == n:
10                return 1 if total == target else 0
11            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
12        
13        return dfs(0, 0)
14