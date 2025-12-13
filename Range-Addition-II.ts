1function maxCount(m: number, n: number, ops: number[][]): number {
2    if (ops.length === 0) return m * n;
3
4    let minRow = m;
5    let minCol = n;
6
7    for (const [a, b] of ops) {
8        minRow = Math.min(minRow, a);
9        minCol = Math.min(minCol, b);
10    }
11
12    return minRow * minCol;
13}