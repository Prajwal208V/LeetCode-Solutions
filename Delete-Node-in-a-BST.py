1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root, key):
9        if not root:
10            return None
11
12        if key < root.val:
13            root.left = self.deleteNode(root.left, key)
14        elif key > root.val:
15            root.right = self.deleteNode(root.right, key)
16        else:
17            if not root.left:
18                return root.right
19            if not root.right:
20                return root.left
21
22            successor = root.right
23            while successor.left:
24                successor = successor.left
25
26            root.val = successor.val
27            root.right = self.deleteNode(root.right, successor.val)
28
29        return root