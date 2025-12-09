1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def getTargetCopy(self, original: 'TreeNode', cloned: 'TreeNode', target: 'TreeNode') -> 'TreeNode':
10        if not original:
11            return None
12        if original is target:
13            return cloned
14        left = self.getTargetCopy(original.left, cloned.left, target)
15        if left:
16            return left
17        return self.getTargetCopy(original.right, cloned.right, target)
18