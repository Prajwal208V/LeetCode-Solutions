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
15function countNodes(root: TreeNode | null): number {
16    if (!root) return 0;
17
18    let l = root, r = root;
19    let hl = 0, hr = 0;
20
21    while (l) {
22        hl++;
23        l = l.left;
24    }
25
26    while (r) {
27        hr++;
28        r = r.right;
29    }
30
31    if (hl === hr) return (1 << hl) - 1;
32
33    return 1 + countNodes(root.left) + countNodes(root.right);
34}
35