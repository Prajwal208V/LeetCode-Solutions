1function maxProfit(prices: number[]): number {
2  let profit = 0
3  for (let i = 1; i < prices.length; i++) {
4    if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1]
5  }
6  return profit
7}