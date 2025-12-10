1function minimumTotal(triangle: number[][]): number {
2    const n = triangle.length;
3    const dp: number[] = new Array(n);
4    for (let i = 0; i < n; i++) {
5        dp[i] = triangle[n - 1][i];
6    }
7    for (let i = n - 2; i >= 0; i--) {
8        for (let j = 0; j <= i; j++) {
9            dp[j] = triangle[i][j] + Math.min(dp[j], dp[j + 1]);
10        }
11    }
12    return dp[0];
13}