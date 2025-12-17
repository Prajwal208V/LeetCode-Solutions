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
15function evaluateTree(root: TreeNode | null): boolean {
16    if (!root) return false
17    if (!root.left && !root.right) return root.val === 1
18    const l = evaluateTree(root.left)
19    const r = evaluateTree(root.right)
20    return root.val === 2 ? l || r : l && r
21}
22