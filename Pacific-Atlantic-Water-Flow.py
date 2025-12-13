1class Solution:
2    def pacificAtlantic(self, heights):
3        if not heights:
4            return []
5
6        m, n = len(heights), len(heights[0])
7        pacific = set()
8        atlantic = set()
9
10        def dfs(r, c, visited, prev):
11            if (
12                r < 0 or r >= m or
13                c < 0 or c >= n or
14                (r, c) in visited or
15                heights[r][c] < prev
16            ):
17                return
18
19            visited.add((r, c))
20            dfs(r + 1, c, visited, heights[r][c])
21            dfs(r - 1, c, visited, heights[r][c])
22            dfs(r, c + 1, visited, heights[r][c])
23            dfs(r, c - 1, visited, heights[r][c])
24
25        for i in range(m):
26            dfs(i, 0, pacific, heights[i][0])
27            dfs(i, n - 1, atlantic, heights[i][n - 1])
28
29        for j in range(n):
30            dfs(0, j, pacific, heights[0][j])
31            dfs(m - 1, j, atlantic, heights[m - 1][j])
32
33        return list(pacific & atlantic)