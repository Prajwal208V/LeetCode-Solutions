1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8from typing import Optional
9
10class TreeNode:
11    def __init__(self, val=0, left=None, right=None):
12        self.val = val
13        self.left = left
14        self.right = right
15
16class Solution:
17    def lowestCommonAncestor(
18        self,
19        root: Optional[TreeNode],
20        p: Optional[TreeNode],
21        q: Optional[TreeNode]
22    ) -> Optional[TreeNode]:
23
24        if not root or root == p or root == q:
25            return root
26
27        left = self.lowestCommonAncestor(root.left, p, q)
28        right = self.lowestCommonAncestor(root.right, p, q)
29
30        if left and right:
31            return root
32        return left if left else right