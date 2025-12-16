1function checkXMatrix(grid: number[][]): boolean {
2    const n = grid.length;
3
4    for (let i = 0; i < n; i++) {
5        for (let j = 0; j < n; j++) {
6            if (i === j || i + j === n - 1) {
7                if (grid[i][j] === 0) return false;
8            } else {
9                if (grid[i][j] !== 0) return false;
10            }
11        }
12    }
13    return true;
14}