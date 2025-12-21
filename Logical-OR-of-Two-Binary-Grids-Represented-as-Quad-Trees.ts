1/**
2 * Definition for _Node.
3 * class _Node {
4 *     val: boolean
5 *     isLeaf: boolean
6 *     topLeft: _Node | null
7 * 	topRight: _Node | null
8 * 	bottomLeft: _Node | null
9 * 	bottomRight: _Node | null
10 * 	constructor(val?: boolean, isLeaf?: boolean, topLeft?: _Node, topRight?: _Node, bottomLeft?: _Node, bottomRight?: _Node) {
11 *         this.val = (val===undefined ? false : val)
12 *         this.isLeaf = (isLeaf===undefined ? false : isLeaf)
13 *         this.topLeft = (topLeft===undefined ? null : topLeft)
14 *         this.topRight = (topRight===undefined ? null : topRight)
15 *         this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
16 *         this.bottomRight = (bottomRight===undefined ? null : bottomRight)
17 *   }
18 * }
19 */
20function intersect(q1: Node | null, q2: Node | null): Node | null {
21    if (!q1) return q2;
22    if (!q2) return q1;
23    if (q1.isLeaf) return q1.val ? q1 : q2;
24    if (q2.isLeaf) return q2.val ? q2 : q1;
25
26    const tl = intersect(q1.topLeft, q2.topLeft);
27    const tr = intersect(q1.topRight, q2.topRight);
28    const bl = intersect(q1.bottomLeft, q2.bottomLeft);
29    const br = intersect(q1.bottomRight, q2.bottomRight);
30
31    if (tl?.isLeaf && tr?.isLeaf && bl?.isLeaf && br?.isLeaf &&
32        tl.val === tr.val && tr.val === bl.val && bl.val === br.val)
33        return new Node(tl.val, true);
34
35    return new Node(false, false, tl!, tr!, bl!, br!);
36}