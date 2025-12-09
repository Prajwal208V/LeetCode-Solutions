1from typing import List
2
3class Solution:
4    def tictactoe(self, moves: List[List[int]]) -> str:
5        rows = [0] * 3
6        cols = [0] * 3
7        diag = 0
8        anti = 0
9        player = 1
10
11        for r, c in moves:
12            rows[r] += player
13            cols[c] += player
14            if r == c:
15                diag += player
16            if r + c == 2:
17                anti += player
18            if 3 in (rows[r], cols[c], diag, anti):
19                return "A"
20            if -3 in (rows[r], cols[c], diag, anti):
21                return "B"
22            player *= -1
23
24        if len(moves) == 9:
25            return "Draw"
26        return "Pending"
27