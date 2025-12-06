1class Solution:
2    def solveSudoku(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows = [0]*9
7        cols = [0]*9
8        boxes = [0]*9
9        empties = []
10        for r in range(9):
11            for c in range(9):
12                if board[r][c] == '.':
13                    empties.append((r,c))
14                else:
15                    d = 1 << (ord(board[r][c]) - ord('1'))
16                    rows[r] |= d
17                    cols[c] |= d
18                    boxes[(r//3)*3 + (c//3)] |= d
19        def dfs(i=0):
20            if i == len(empties):
21                return True
22            r,c = empties[i]
23            used = rows[r] | cols[c] | boxes[(r//3)*3 + (c//3)]
24            mask = (~used) & 0x1FF
25            while mask:
26                bit = mask & -mask
27                mask -= bit
28                d = (bit.bit_length() - 1)
29                ch = chr(ord('1') + d)
30                rows[r] |= bit
31                cols[c] |= bit
32                boxes[(r//3)*3 + (c//3)] |= bit
33                board[r][c] = ch
34                if dfs(i+1):
35                    return True
36                rows[r] &= ~bit
37                cols[c] &= ~bit
38                boxes[(r//3)*3 + (c//3)] &= ~bit
39                board[r][c] = '.'
40            return False
41        dfs()
42        