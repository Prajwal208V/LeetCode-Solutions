1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class BSTIterator:
8    def __init__(self, root: Optional[TreeNode]):
9        self.stack = []
10        self._leftmost(root)
11
12    def _leftmost(self, node):
13        while node:
14            self.stack.append(node)
15            node = node.left
16
17    def next(self) -> int:
18        node = self.stack.pop()
19        if node.right:
20            self._leftmost(node.right)
21        return node.val
22
23    def hasNext(self) -> bool:
24        return len(self.stack) > 0
25
26# Your BSTIterator object will be instantiated and called as such:
27# obj = BSTIterator(root)
28# param_1 = obj.next()
29# param_2 = obj.hasNext()