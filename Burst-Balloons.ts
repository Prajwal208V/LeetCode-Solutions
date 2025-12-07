1function maxCoins(nums: number[]): number {
2    const arr = [1, ...nums.filter(x => x > 0), 1];
3    const n = arr.length;
4    const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
5
6    for (let len = 2; len < n; len++) {
7        for (let left = 0; left + len < n; left++) {
8            const right = left + len;
9            for (let k = left + 1; k < right; k++) {
10                dp[left][right] = Math.max(
11                    dp[left][right],
12                    dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]
13                );
14            }
15        }
16    }
17
18    return dp[0][n - 1];
19}
20