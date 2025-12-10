1class Solution:
2    def isPathCrossing(self, path: str) -> bool:
3        x = y = 0
4        seen = {(0, 0)}
5        for c in path:
6            if c == 'N':
7                y += 1
8            elif c == 'S':
9                y -= 1
10            elif c == 'E':
11                x += 1
12            else:
13                x -= 1
14            if (x, y) in seen:
15                return True
16            seen.add((x, y))
17        return False