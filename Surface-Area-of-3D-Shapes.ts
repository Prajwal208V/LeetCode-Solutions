1function surfaceArea(grid: number[][]): number {
2    const n = grid.length;
3    let res = 0;
4
5    for (let i = 0; i < n; i++) {
6        for (let j = 0; j < n; j++) {
7            const v = grid[i][j];
8            if (v === 0) continue;
9            res += v * 4 + 2;
10            if (i > 0) res -= 2 * Math.min(v, grid[i - 1][j]);
11            if (j > 0) res -= 2 * Math.min(v, grid[i][j - 1]);
12        }
13    }
14
15    return res;
16}
17