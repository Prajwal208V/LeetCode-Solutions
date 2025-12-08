1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
9        self.prev = None
10        self.min_diff = float('inf')
11        
12        def inorder(node):
13            if not node:
14                return
15            
16            # Traverse left subtree
17            inorder(node.left)
18            
19            # Process current node
20            if self.prev is not None:
21                self.min_diff = min(self.min_diff, node.val - self.prev)
22            self.prev = node.val
23            
24            # Traverse right subtree
25            inorder(node.right)
26        
27        inorder(root)
28        return self.min_diff