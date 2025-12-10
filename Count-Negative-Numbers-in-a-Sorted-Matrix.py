1from typing import List
2
3class Solution:
4    def countNegatives(self, grid: List[List[int]]) -> int:
5        m, n = len(grid), len(grid[0])
6        i, j = m - 1, 0
7        ans = 0
8        while i >= 0 and j < n:
9            if grid[i][j] < 0:
10                ans += n - j
11                i -= 1
12            else:
13                j += 1
14        return ans
15