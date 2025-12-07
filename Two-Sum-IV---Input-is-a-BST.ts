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
15function findTarget(root: TreeNode | null, k: number): boolean {
16    const set = new Set<number>();
17
18    function dfs(node: TreeNode | null): boolean {
19        if (!node) return false;
20        if (set.has(k - node.val)) return true;
21        set.add(node.val);
22        return dfs(node.left) || dfs(node.right);
23    }
24
25    return dfs(root);
26}
27