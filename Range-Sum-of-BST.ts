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
14function rangeSumBST(root: TreeNode | null, low: number, high: number): number {
15    if (!root) return 0;
16    let sum = 0;
17
18    function dfs(node: TreeNode | null) {
19        if (!node) return;
20        if (node.val >= low && node.val <= high) sum += node.val;
21        if (node.val > low) dfs(node.left);
22        if (node.val < high) dfs(node.right);
23    }
24
25    dfs(root);
26    return sum;
27}
28