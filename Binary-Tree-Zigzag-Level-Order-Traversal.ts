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
15function zigzagLevelOrder(root: TreeNode | null): number[][] {
16    if (!root) return [];
17    const res: number[][] = [];
18    const q: TreeNode[] = [root];
19    let leftToRight = true;
20    while (q.length) {
21        const size = q.length;
22        const level: number[] = new Array(size);
23        for (let i = 0; i < size; i++) {
24            const node = q.shift() as TreeNode;
25            const idx = leftToRight ? i : size - 1 - i;
26            level[idx] = node.val;
27            if (node.left) q.push(node.left);
28            if (node.right) q.push(node.right);
29        }
30        res.push(level);
31        leftToRight = !leftToRight;
32    }
33    return res;
34}
35