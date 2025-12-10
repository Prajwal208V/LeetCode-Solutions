1class NumMatrix {
2    private prefix: number[][];
3
4    constructor(matrix: number[][]) {
5        const m = matrix.length;
6        const n = m === 0 ? 0 : matrix[0].length;
7        this.prefix = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
8
9        for (let i = 1; i <= m; i++) {
10            for (let j = 1; j <= n; j++) {
11                this.prefix[i][j] =
12                    matrix[i - 1][j - 1] +
13                    this.prefix[i - 1][j] +
14                    this.prefix[i][j - 1] -
15                    this.prefix[i - 1][j - 1];
16            }
17        }
18    }
19
20    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
21        const r1 = row1 + 1;
22        const c1 = col1 + 1;
23        const r2 = row2 + 1;
24        const c2 = col2 + 1;
25
26        return (
27            this.prefix[r2][c2] -
28            this.prefix[r1 - 1][c2] -
29            this.prefix[r2][c1 - 1] +
30            this.prefix[r1 - 1][c1 - 1]
31        );
32    }
33}
34
35
36/**
37 * Your NumMatrix object will be instantiated and called as such:
38 * var obj = new NumMatrix(matrix)
39 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
40 */