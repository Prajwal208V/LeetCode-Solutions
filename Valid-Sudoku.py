1from typing import List
2
3class Solution:
4    def isValidSudoku(self, board: List[List[str]]) -> bool:
5        rows = [set() for _ in range(9)]
6        cols = [set() for _ in range(9)]
7        boxes = [set() for _ in range(9)]
8        for r in range(9):
9            for c in range(9):
10                v = board[r][c]
11                if v == '.':
12                    continue
13                if v in rows[r] or v in cols[c] or v in boxes[(r//3)*3 + (c//3)]:
14                    return False
15                rows[r].add(v)
16                cols[c].add(v)
17                boxes[(r//3)*3 + (c//3)].add(v)
18        return True