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
15function sumRootToLeaf(root: TreeNode | null): number {
16    let sum = 0;
17
18    function dfs(node: TreeNode | null, cur: number): void {
19        if (!node) return;
20        cur = (cur << 1) | node.val;
21        if (!node.left && !node.right) {
22            sum += cur;
23            return;
24        }
25        dfs(node.left, cur);
26        dfs(node.right, cur);
27    }
28
29    dfs(root, 0);
30    return sum;
31}
32