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
16    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
17        stack = []
18        cur = root
19
20        while True:
21            while cur:
22                stack.append(cur)
23                cur = cur.left
24            cur = stack.pop()
25            k -= 1
26            if k == 0:
27                return cur.val
28            cur = cur.right