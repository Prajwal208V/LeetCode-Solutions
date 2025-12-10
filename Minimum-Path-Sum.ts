1function minPathSum(grid: number[][]): number {
2    const m = grid.length;
3    const n = grid[0].length;
4    const dp: number[] = new Array(n).fill(0);
5    dp[0] = grid[0][0];
6
7    for (let j = 1; j < n; j++) {
8        dp[j] = dp[j - 1] + grid[0][j];
9    }
10
11    for (let i = 1; i < m; i++) {
12        dp[0] += grid[i][0];
13        for (let j = 1; j < n; j++) {
14            dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
15        }
16    }
17
18    return dp[n - 1];
19}