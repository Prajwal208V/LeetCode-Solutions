1function change(amount: number, coins: number[]): number {
2    const dp = new Array(amount + 1).fill(0)
3    dp[0] = 1
4
5    for (const coin of coins) {
6        for (let i = coin; i <= amount; i++) {
7            dp[i] += dp[i - coin]
8        }
9    }
10
11    return dp[amount]
12}