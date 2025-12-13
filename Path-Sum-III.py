1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from typing import Optional
8from collections import defaultdict
9
10class TreeNode:
11    def __init__(self, val=0, left=None, right=None):
12        self.val = val
13        self.left = left
14        self.right = right
15
16class Solution:
17    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
18        prefix = defaultdict(int)
19        prefix[0] = 1
20
21        def dfs(node, curr_sum):
22            if not node:
23                return 0
24
25            curr_sum += node.val
26            res = prefix[curr_sum - targetSum]
27
28            prefix[curr_sum] += 1
29            res += dfs(node.left, curr_sum)
30            res += dfs(node.right, curr_sum)
31            prefix[curr_sum] -= 1
32
33            return res
34
35        return dfs(root, 0)