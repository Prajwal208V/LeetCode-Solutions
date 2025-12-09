1from typing import List
2
3class Solution:
4    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
5        m, n = len(grid), len(grid[0])
6        total = m * n
7        k %= total
8        if k == 0:
9            return grid
10        flat = [grid[i][j] for i in range(m) for j in range(n)]
11        flat = flat[-k:] + flat[:-k]
12        return [flat[i * n:(i + 1) * n] for i in range(m)]
13