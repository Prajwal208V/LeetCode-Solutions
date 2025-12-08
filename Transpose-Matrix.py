1class Solution:
2    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
3        m, n = len(matrix), len(matrix[0])
4        res = [[0] * m for _ in range(n)]
5        for i in range(m):
6            for j in range(n):
7                res[j][i] = matrix[i][j]
8        return res
9