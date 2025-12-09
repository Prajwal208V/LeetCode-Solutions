1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        x = y = 0
4        for c in moves:
5            if c == 'U':
6                y += 1
7            elif c == 'D':
8                y -= 1
9            elif c == 'L':
10                x -= 1
11            elif c == 'R':
12                x += 1
13        return x == 0 and y == 0