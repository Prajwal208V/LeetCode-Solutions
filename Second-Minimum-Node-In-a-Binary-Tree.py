1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
9        first = root.val
10        ans = float('inf')
11
12        def dfs(node: Optional[TreeNode]) -> None:
13            nonlocal ans
14            if not node:
15                return
16            if first < node.val < ans:
17                ans = node.val
18            elif node.val == first:
19                dfs(node.left)
20                dfs(node.right)
21
22        dfs(root)
23        return ans if ans < float('inf') else -1
24