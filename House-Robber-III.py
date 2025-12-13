1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from typing import Optional
8
9class TreeNode:
10    def __init__(self, val=0, left=None, right=None):
11        self.val = val
12        self.left = left
13        self.right = right
14
15class Solution:
16    def rob(self, root: Optional[TreeNode]) -> int:
17        def dfs(node):
18            if not node:
19                return (0, 0)
20
21            left = dfs(node.left)
22            right = dfs(node.right)
23
24            rob_node = node.val + left[1] + right[1]
25            skip_node = max(left) + max(right)
26
27            return (rob_node, skip_node)
28
29        return max(dfs(root))