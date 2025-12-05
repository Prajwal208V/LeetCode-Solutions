1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        def backtrack(path, used):
5            if len(path) == len(nums):
6                res.append(path[:])
7                return
8            for i in range(len(nums)):
9                if i in used:
10                    continue
11                used.add(i)
12                path.append(nums[i])
13                backtrack(path, used)
14                path.pop()
15                used.remove(i)
16        backtrack([], set())
17        return res