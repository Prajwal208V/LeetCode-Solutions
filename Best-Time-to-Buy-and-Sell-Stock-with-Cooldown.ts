1function maxProfit(prices: number[]): number {
2    if (prices.length === 0) return 0;
3    let hold = -prices[0];
4    let sold = 0;
5    let rest = 0;
6
7    for (let i = 1; i < prices.length; i++) {
8        const prevHold = hold;
9        const prevSold = sold;
10        const prevRest = rest;
11
12        hold = Math.max(prevHold, prevRest - prices[i]);
13        sold = prevHold + prices[i];
14        rest = Math.max(prevRest, prevSold);
15    }
16
17    return Math.max(sold, rest);
18}