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
15function averageOfLevels(root: TreeNode | null): number[] {
16    if (!root) return [];
17    const res: number[] = [];
18    const q: TreeNode[] = [root];
19    while (q.length) {
20        let sum = 0;
21        const size = q.length;
22        for (let i = 0; i < size; i++) {
23            const node = q.shift() as TreeNode;
24            sum += node.val;
25            if (node.left) q.push(node.left);
26            if (node.right) q.push(node.right);
27        }
28        res.push(sum / size);
29    }
30    return res;
31}
32