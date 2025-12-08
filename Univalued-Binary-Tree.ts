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
15function isUnivalTree(root: TreeNode | null): boolean {
16    if (!root) return true;
17    const val = root.val;
18
19    function dfs(node: TreeNode | null): boolean {
20        if (!node) return true;
21        if (node.val !== val) return false;
22        return dfs(node.left) && dfs(node.right);
23    }
24
25    return dfs(root);
26}
27