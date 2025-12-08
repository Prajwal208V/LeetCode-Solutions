1class Solution:
2    def projectionArea(self, grid: list[list[int]]) -> int:
3        n = len(grid)
4        top = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
5        front = sum(max(row) for row in grid)
6        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
7        return top + front + side
8