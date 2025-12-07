1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def generateTrees(self, n: int):
9        if n == 0:
10            return []
11        from functools import lru_cache
12
13        @lru_cache(None)
14        def build(lo, hi):
15            if lo > hi:
16                return [None]
17            res = []
18            for root_val in range(lo, hi + 1):
19                left_trees = build(lo, root_val - 1)
20                right_trees = build(root_val + 1, hi)
21                for l in left_trees:
22                    for r in right_trees:
23                        root = TreeNode(root_val)
24                        root.left = l
25                        root.right = r
26                        res.append(root)
27            return res
28
29        return build(1, n)
30