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
15function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
16    if (!subRoot) return true;
17    if (!root) return false;
18
19    function isSame(a: TreeNode | null, b: TreeNode | null): boolean {
20        if (!a && !b) return true;
21        if (!a || !b) return false;
22        if (a.val !== b.val) return false;
23        return isSame(a.left, b.left) && isSame(a.right, b.right);
24    }
25
26    if (isSame(root, subRoot)) return true;
27    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
28}
29