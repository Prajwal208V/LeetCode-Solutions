1class Solution:
2    def findSubsequences(self, nums):
3        res = []
4
5        def dfs(start, path):
6            if len(path) >= 2:
7                res.append(path[:])
8
9            used = set()
10            for i in range(start, len(nums)):
11                if (path and nums[i] < path[-1]) or nums[i] in used:
12                    continue
13                used.add(nums[i])
14                dfs(i + 1, path + [nums[i]])
15
16        dfs(0, [])
17        return res