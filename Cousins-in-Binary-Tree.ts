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
15function isCousins(root: TreeNode | null, x: number, y: number): boolean {
16    if (!root) return false;
17    const q: (TreeNode | null)[] = [root];
18
19    while (q.length) {
20        const size = q.length;
21        let parentX: TreeNode | null = null;
22        let parentY: TreeNode | null = null;
23
24        for (let i = 0; i < size; i++) {
25            const node = q.shift() as TreeNode;
26            if (node.left) {
27                if (node.left.val === x) parentX = node;
28                if (node.left.val === y) parentY = node;
29                q.push(node.left);
30            }
31            if (node.right) {
32                if (node.right.val === x) parentX = node;
33                if (node.right.val === y) parentY = node;
34                q.push(node.right);
35            }
36        }
37
38        if (parentX && parentY) return parentX !== parentY;
39        if (parentX || parentY) return false;
40    }
41
42    return false;
43}
44