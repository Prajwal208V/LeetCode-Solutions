1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
5        self.val = val
6        self.children = children
7"""
8
9from typing import List
10from collections import deque
11
12class Node:
13    def __init__(self, val=None, children=None):
14        self.val = val
15        self.children = children if children is not None else []
16
17class Solution:
18    def levelOrder(self, root: 'Node') -> List[List[int]]:
19        if not root:
20            return []
21
22        res = []
23        q = deque([root])
24
25        while q:
26            level = []
27            for _ in range(len(q)):
28                node = q.popleft()
29                level.append(node.val)
30                for child in node.children:
31                    q.append(child)
32            res.append(level)
33
34        return res