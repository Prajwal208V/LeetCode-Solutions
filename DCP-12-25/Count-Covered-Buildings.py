1from typing import List, Tuple
2from collections import defaultdict
3
4class Solution:
5    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
6        row_min = {}
7        row_max = {}
8        col_min = {}
9        col_max = {}
10        pts = set()
11
12        for x, y in buildings:
13            pts.add((x, y))
14            if x in row_min:
15                if y < row_min[x]: row_min[x] = y
16                if y > row_max[x]: row_max[x] = y
17            else:
18                row_min[x] = row_max[x] = y
19            if y in col_min:
20                if x < col_min[y]: col_min[y] = x
21                if x > col_max[y]: col_max[y] = x
22            else:
23                col_min[y] = col_max[y] = x
24
25        cnt = 0
26        for x, y in pts:
27            if y > row_min[x] and y < row_max[x] and x > col_min[y] and x < col_max[y]:
28                cnt += 1
29
30        return cnt
31