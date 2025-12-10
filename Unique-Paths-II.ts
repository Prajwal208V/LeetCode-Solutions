1function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
2    const m = obstacleGrid.length;
3    const n = obstacleGrid[0].length;
4    const dp: number[] = new Array(n).fill(0);
5    dp[0] = obstacleGrid[0][0] === 1 ? 0 : 1;
6
7    for (let i = 0; i < m; i++) {
8        for (let j = 0; j < n; j++) {
9            if (obstacleGrid[i][j] === 1) {
10                dp[j] = 0;
11            } else if (j > 0) {
12                dp[j] += dp[j - 1];
13            }
14        }
15    }
16
17    return dp[n - 1];
18}