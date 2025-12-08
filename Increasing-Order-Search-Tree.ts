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
15function increasingBST(root: TreeNode | null): TreeNode | null {
16    const dummy = new TreeNode(0);
17    let cur = dummy;
18
19    function inorder(node: TreeNode | null): void {
20        if (!node) return;
21        inorder(node.left);
22        cur.right = new TreeNode(node.val);
23        cur = cur.right;
24        inorder(node.right);
25    }
26
27    inorder(root);
28    return dummy.right;
29}
30