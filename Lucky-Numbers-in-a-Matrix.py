1from typing import List
2
3class Solution:
4    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
5        row_mins = [min(row) for row in matrix]
6        col_max = [max(col) for col in zip(*matrix)]
7        res = []
8        for i, row in enumerate(matrix):
9            for j, v in enumerate(row):
10                if v == row_mins[i] and v == col_max[j]:
11                    res.append(v)
12        return res
13