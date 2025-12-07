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
15/**
16 Do not return anything, modify root in-place instead.
17 */
18function flatten(root: TreeNode | null): void {
19    let prev: TreeNode | null = null;
20
21    function dfs(node: TreeNode | null): void {
22        if (!node) return;
23        dfs(node.right);
24        dfs(node.left);
25        node.right = prev;
26        node.left = null;
27        prev = node;
28    }
29
30    dfs(root);
31}
32