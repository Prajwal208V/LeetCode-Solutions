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
15function findBottomLeftValue(root: TreeNode | null): number {
16    let queue: TreeNode[] = [root!]
17    let res = root!.val
18
19    while (queue.length) {
20        let size = queue.length
21        res = queue[0].val
22        for (let i = 0; i < size; i++) {
23            const node = queue.shift()!
24            if (node.left) queue.push(node.left)
25            if (node.right) queue.push(node.right)
26        }
27    }
28    return res
29}
30