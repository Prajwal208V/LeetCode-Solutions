1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8class Solution:
9    def cloneGraph(self, node: 'Node') -> 'Node':
10        if not node:
11            return None
12        old_to_new = {}
13
14        def dfs(n: 'Node') -> 'Node':
15            if n in old_to_new:
16                return old_to_new[n]
17            copy = Node(n.val)
18            old_to_new[n] = copy
19            for nei in n.neighbors:
20                copy.neighbors.append(dfs(nei))
21            return copy
22
23        return dfs(node)
24