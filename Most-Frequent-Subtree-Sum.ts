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
15function findFrequentTreeSum(root: TreeNode | null): number[] {
16    const freq = new Map<number, number>();
17    let maxFreq = 0;
18
19    function dfs(node: TreeNode | null): number {
20        if (!node) return 0;
21        const sum = node.val + dfs(node.left) + dfs(node.right);
22        freq.set(sum, (freq.get(sum) || 0) + 1);
23        maxFreq = Math.max(maxFreq, freq.get(sum)!);
24        return sum;
25    }
26
27    dfs(root);
28    return [...freq.entries()].filter(([_, v]) => v === maxFreq).map(([k]) => k);
29}