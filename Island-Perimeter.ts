1function islandPerimeter(grid: number[][]): number {
2    const m = grid.length;
3    const n = grid[0].length;
4    let peri = 0;
5    for (let i = 0; i < m; i++) {
6        for (let j = 0; j < n; j++) {
7            if (grid[i][j] === 1) {
8                peri += 4;
9                if (i > 0 && grid[i - 1][j] === 1) peri -= 2;
10                if (j > 0 && grid[i][j - 1] === 1) peri -= 2;
11            }
12        }
13    }
14    return peri;
15}