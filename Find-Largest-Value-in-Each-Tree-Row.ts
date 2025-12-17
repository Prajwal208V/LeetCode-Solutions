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
14function largestValues(root: TreeNode | null): number[] {
15    if (!root) return []
16    let res: number[] = []
17    let queue: TreeNode[] = [root]
18
19    while (queue.length) {
20        let size = queue.length
21        let maxVal = -Infinity
22        for (let i = 0; i < size; i++) {
23            const node = queue.shift()!
24            maxVal = Math.max(maxVal, node.val)
25            if (node.left) queue.push(node.left)
26            if (node.right) queue.push(node.right)
27        }
28        res.push(maxVal)
29    }
30    return res
31}