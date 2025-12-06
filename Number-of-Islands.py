1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid or not grid[0]:
4            return 0
5        m, n = len(grid), len(grid[0])
6        islands = 0
7
8        def dfs(i: int, j: int) -> None:
9            stack = [(i, j)]
10            while stack:
11                x, y = stack.pop()
12                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
13                    grid[x][y] = '0'
14                    stack.append((x+1, y))
15                    stack.append((x-1, y))
16                    stack.append((x, y+1))
17                    stack.append((x, y-1))
18
19        for i in range(m):
20            for j in range(n):
21                if grid[i][j] == '1':
22                    islands += 1
23                    dfs(i, j)
24
25        return islands
26