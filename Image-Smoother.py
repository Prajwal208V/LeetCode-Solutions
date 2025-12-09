1class Solution:
2    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
3        m, n = len(img), len(img[0])
4        res = [[0] * n for _ in range(m)]
5        for i in range(m):
6            for j in range(n):
7                s = cnt = 0
8                for x in range(i - 1, i + 2):
9                    for y in range(j - 1, j + 2):
10                        if 0 <= x < m and 0 <= y < n:
11                            s += img[x][y]
12                            cnt += 1
13                res[i][j] = s // cnt
14        return res