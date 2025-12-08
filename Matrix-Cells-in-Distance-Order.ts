1function allCellsDistOrder(R: number, C: number, r0: number, c0: number): number[][] {
2    const res: number[][] = [];
3    for (let r = 0; r < R; r++) {
4        for (let c = 0; c < C; c++) {
5            res.push([r, c]);
6        }
7    }
8    res.sort(
9        ([r1, c1], [r2, c2]) =>
10            Math.abs(r1 - r0) + Math.abs(c1 - c0) - (Math.abs(r2 - r0) + Math.abs(c2 - c0))
11    );
12    return res;
13}
14