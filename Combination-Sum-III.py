1from typing import List
2
3class Solution:
4    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
5        res = []
6
7        def backtrack(start: int, path: List[int], total: int):
8            if len(path) == k:
9                if total == n:
10                    res.append(path[:])
11                return
12            for i in range(start, 10):
13                if total + i > n:
14                    break
15                backtrack(i + 1, path + [i], total + i)
16
17        backtrack(1, [], 0)
18        return res