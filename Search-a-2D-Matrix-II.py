1from typing import List
2
3class Solution:
4    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
5        if not matrix or not matrix[0]:
6            return False
7
8        r, c = 0, len(matrix[0]) - 1
9
10        while r < len(matrix) and c >= 0:
11            if matrix[r][c] == target:
12                return True
13            elif matrix[r][c] > target:
14                c -= 1
15            else:
16                r += 1
17
18        return False