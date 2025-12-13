1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9    def serialize(self, root):
10        vals = []
11
12        def dfs(node):
13            if not node:
14                return
15            vals.append(str(node.val))
16            dfs(node.left)
17            dfs(node.right)
18
19        dfs(root)
20        return ",".join(vals)
21
22    def deserialize(self, data):
23        if not data:
24            return None
25
26        vals = list(map(int, data.split(",")))
27        i = 0
28
29        def build(lower, upper):
30            nonlocal i
31            if i == len(vals):
32                return None
33            val = vals[i]
34            if val < lower or val > upper:
35                return None
36
37            i += 1
38            node = TreeNode(val)
39            node.left = build(lower, val)
40            node.right = build(val, upper)
41            return node
42
43        return build(float("-inf"), float("inf"))
44
45# Your Codec object will be instantiated and called as such:
46# Your Codec object will be instantiated and called as such:
47# ser = Codec()
48# deser = Codec()
49# tree = ser.serialize(root)
50# ans = deser.deserialize(tree)
51# return ans