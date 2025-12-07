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
15function searchBST(root: TreeNode | null, val: number): TreeNode | null {
16    let node: TreeNode | null = root;
17    while (node) {
18        if (node.val === val) return node;
19        if (val < node.val) node = node.left;
20        else node = node.right;
21    }
22    return null;
23}
24