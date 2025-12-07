1from typing import List
2from functools import lru_cache
3
4class Solution:
5    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
6        if not matrix or not matrix[0]:
7            return 0
8        m, n = len(matrix), len(matrix[0])
9
10        @lru_cache(None)
11        def dfs(i: int, j: int) -> int:
12            cur = matrix[i][j]
13            best = 1
14            if i > 0 and matrix[i-1][j] > cur:
15                best = max(best, 1 + dfs(i-1, j))
16            if i + 1 < m and matrix[i+1][j] > cur:
17                best = max(best, 1 + dfs(i+1, j))
18            if j > 0 and matrix[i][j-1] > cur:
19                best = max(best, 1 + dfs(i, j-1))
20            if j + 1 < n and matrix[i][j+1] > cur:
21                best = max(best, 1 + dfs(i, j+1))
22            return best
23
24        ans = 0
25        for i in range(m):
26            for j in range(n):
27                ans = max(ans, dfs(i, j))
28        return ans
29