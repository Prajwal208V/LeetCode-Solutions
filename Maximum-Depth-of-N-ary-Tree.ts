1/**
2 * Definition for _Node.
3 * class _Node {
4 *     val: number
5 *     children: _Node[]
6 * 
7 *     constructor(val?: number, children?: _Node[]) {
8 *         this.val = (val===undefined ? 0 : val)
9 *         this.children = (children===undefined ? [] : children)
10 *     }
11 * }
12 */
13
14function maxDepth(root: Node | null): number {
15    if (!root) return 0;
16    if (!root.children || root.children.length === 0) return 1;
17    let depth = 0;
18    for (const child of root.children) {
19        depth = Math.max(depth, maxDepth(child));
20    }
21    return depth + 1;
22}
23