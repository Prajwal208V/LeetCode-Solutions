1"""
2# Definition for a QuadTree node.
3class Node:
4    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
5        self.val = val
6        self.isLeaf = isLeaf
7        self.topLeft = topLeft
8        self.topRight = topRight
9        self.bottomLeft = bottomLeft
10        self.bottomRight = bottomRight
11"""
12
13from typing import List, Optional
14
15class Node:
16    def __init__(self, val: bool, isLeaf: bool,
17                 topLeft: Optional['Node'] = None,
18                 topRight: Optional['Node'] = None,
19                 bottomLeft: Optional['Node'] = None,
20                 bottomRight: Optional['Node'] = None):
21        self.val = val
22        self.isLeaf = isLeaf
23        self.topLeft = topLeft
24        self.topRight = topRight
25        self.bottomLeft = bottomLeft
26        self.bottomRight = bottomRight
27
28
29class Solution:
30    def construct(self, grid: List[List[int]]) -> 'Node':
31        n = len(grid)
32
33        def build(r: int, c: int, size: int) -> Node:
34            first = grid[r][c]
35            same = True
36            for i in range(r, r + size):
37                for j in range(c, c + size):
38                    if grid[i][j] != first:
39                        same = False
40                        break
41                if not same:
42                    break
43
44            if same:
45                return Node(first == 1, True)
46
47            half = size // 2
48            return Node(
49                True,
50                False,
51                build(r, c, half),
52                build(r, c + half, half),
53                build(r + half, c, half),
54                build(r + half, c + half, half)
55            )
56
57        return build(0, 0, n)