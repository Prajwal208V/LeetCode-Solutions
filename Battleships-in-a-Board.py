1from typing import List
2
3class Solution:
4    def countBattleships(self, board: List[List[str]]) -> int:
5        if not board or not board[0]:
6            return 0
7
8        m, n = len(board), len(board[0])
9        count = 0
10
11        for i in range(m):
12            for j in range(n):
13                if board[i][j] == 'X':
14                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
15                        count += 1
16
17        return count