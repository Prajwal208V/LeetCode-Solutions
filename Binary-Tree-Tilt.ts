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
15function findTilt(root: TreeNode | null): number {
16    let tilt = 0;
17
18    function dfs(node: TreeNode | null): number {
19        if (!node) return 0;
20        const left = dfs(node.left);
21        const right = dfs(node.right);
22        tilt += Math.abs(left - right);
23        return left + right + node.val;
24    }
25
26    dfs(root);
27    return tilt;
28}
29