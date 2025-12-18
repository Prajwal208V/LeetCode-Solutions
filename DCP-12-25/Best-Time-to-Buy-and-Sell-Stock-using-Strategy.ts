1function maxProfit(prices: number[], strategy: number[], k: number): number {
2    const n = prices.length
3    const half = k / 2
4
5    const profitSum = new Array(n + 1).fill(0)
6    const priceSum = new Array(n + 1).fill(0)
7
8    for (let i = 0; i < n; i++) {
9        profitSum[i + 1] = profitSum[i] + strategy[i] * prices[i]
10        priceSum[i + 1] = priceSum[i] + prices[i]
11    }
12
13    let ans = profitSum[n]
14
15    for (let i = k - 1; i < n; i++) {
16        const left = i - k + 1
17
18        const before = profitSum[left]
19
20        const sellPart =
21            priceSum[i + 1] - priceSum[i - half + 1]
22
23        const after = profitSum[n] - profitSum[i + 1]
24
25        ans = Math.max(ans, before + sellPart + after)
26    }
27
28    return ans
29}