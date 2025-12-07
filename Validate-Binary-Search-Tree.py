1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        def helper(node, low, high):
10            if not node:
11                return True
12            if not (low < node.val < high):
13                return False
14            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
15        return helper(root, float('-inf'), float('inf'))
16
17        