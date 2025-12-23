1class Solution:
2    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
3        for row in grid:
4            row.sort()
5        res = 0
6        for c in range(len(grid[0])):
7            res += max(row[c] for row in grid)
8        return res