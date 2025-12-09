1from typing import List, Optional
2
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8
9class Solution:
10    def findMode(self, root: Optional['TreeNode']) -> List[int]:
11        if not root:
12            return []
13        
14        self.prev = None
15        self.count = 0
16        self.max_count = 0
17        self.modes = []
18
19        def inorder(node):
20            if not node:
21                return
22            inorder(node.left)
23            if self.prev is None or self.prev != node.val:
24                self.count = 1
25            else:
26                self.count += 1
27            if self.count > self.max_count:
28                self.max_count = self.count
29                self.modes = [node.val]
30            elif self.count == self.max_count:
31                self.modes.append(node.val)
32            self.prev = node.val
33            inorder(node.right)
34
35        inorder(root)
36        return self.modes
37