1from typing import List
2
3class Solution:
4    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
5        rows = [0] * m
6        cols = [0] * n
7        for r, c in indices:
8            rows[r] ^= 1
9            cols[c] ^= 1
10        odd_rows = sum(rows)
11        odd_cols = sum(cols)
12        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
13