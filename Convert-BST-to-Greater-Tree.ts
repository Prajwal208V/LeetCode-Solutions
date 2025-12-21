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
15function convertBST(root: TreeNode | null): TreeNode | null {
16    let sum = 0;
17    function dfs(node: TreeNode | null): void {
18        if (!node) return;
19        dfs(node.right);
20        sum += node.val;
21        node.val = sum;
22        dfs(node.left);
23    }
24    dfs(root);
25    return root;
26}