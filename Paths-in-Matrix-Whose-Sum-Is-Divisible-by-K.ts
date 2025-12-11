1function numberOfPaths(grid: number[][], k: number): number {
2  const MOD = 1_000_000_007
3  const m = grid.length
4  const n = grid[0].length
5  const dp: number[][][] = Array.from({ length: m }, () => Array.from({ length: n }, () => Array(k).fill(0)))
6  dp[0][0][grid[0][0] % k] = 1
7  for (let i = 0; i < m; i++) {
8    for (let j = 0; j < n; j++) {
9      const cur = dp[i][j]
10      if (i === m - 1 && j === n - 1) continue
11      for (let r = 0; r < k; r++) {
12        const cnt = cur[r]
13        if (!cnt) continue
14        if (i + 1 < m) {
15          const nr = (r + grid[i + 1][j]) % k
16          dp[i + 1][j][nr] = (dp[i + 1][j][nr] + cnt) % MOD
17        }
18        if (j + 1 < n) {
19          const nr = (r + grid[i][j + 1]) % k
20          dp[i][j + 1][nr] = (dp[i][j + 1][nr] + cnt) % MOD
21        }
22      }
23    }
24  }
25  return dp[m - 1][n - 1][0] % MOD
26}