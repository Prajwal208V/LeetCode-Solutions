1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        orig = image[sr][sc]
4        if orig == color:
5            return image
6        rows, cols = len(image), len(image[0])
7        def dfs(r, c):
8            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != orig:
9                return
10            image[r][c] = color
11            dfs(r+1, c)
12            dfs(r-1, c)
13            dfs(r, c+1)
14            dfs(r, c-1)
15        dfs(sr, sc)
16        return image