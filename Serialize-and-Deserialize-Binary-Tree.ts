1/**
2 * Definition for a binary tree node.
3 * class TreeNode {
4 *     val: number
5 *     left: TreeNode | null
6 *     right: TreeNode | null
7 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
8 *         this.val = (val===undefined ? 0 : val)
9 *         this.left = (left===undefined ? null : left)
10 *         this.right = (right===undefined ? null : right)
11 *     }
12 * }
13 */
14
15/*
16 * Encodes a tree to a single string.
17 */
18function serialize(root: TreeNode | null): string {
19  if (!root) return "";
20  const q: (TreeNode | null)[] = [root];
21  const res: string[] = [];
22  while (q.length) {
23    const node = q.shift()!;
24    if (node) {
25      res.push(String(node.val));
26      q.push(node.left, node.right);
27    } else {
28      res.push("null");
29    }
30  }
31  let i = res.length - 1;
32  while (i >= 0 && res[i] === "null") i--;
33  return res.slice(0, i + 1).join(",");
34}
35/*
36 * Decodes your encoded data to tree.
37 */
38function deserialize(data: string): TreeNode | null {
39  if (!data) return null;
40  const vals = data.split(",");
41  const root = new TreeNode(Number(vals[0]));
42  const q: TreeNode[] = [root];
43  let i = 1;
44  while (i < vals.length) {
45    const node = q.shift()!;
46    const leftVal = vals[i++];
47    if (leftVal !== "null") {
48      const leftNode = new TreeNode(Number(leftVal));
49      node.left = leftNode;
50      q.push(leftNode);
51    }
52    if (i < vals.length) {
53      const rightVal = vals[i++];
54      if (rightVal !== "null") {
55        const rightNode = new TreeNode(Number(rightVal));
56        node.right = rightNode;
57        q.push(rightNode);
58      }
59    }
60  }
61  return root;
62}
63
64
65/**
66 * Your functions will be called as such:
67 * deserialize(serialize(root));
68 */