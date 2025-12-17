1function longestPalindromeSubseq(s: string): number {
2    const n = s.length
3    const dp = Array.from({ length: n }, () => Array(n).fill(0))
4
5    for (let i = n - 1; i >= 0; i--) {
6        dp[i][i] = 1
7        for (let j = i + 1; j < n; j++) {
8            if (s[i] === s[j]) {
9                dp[i][j] = dp[i + 1][j - 1] + 2
10            } else {
11                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1])
12            }
13        }
14    }
15    return dp[0][n - 1]
16}