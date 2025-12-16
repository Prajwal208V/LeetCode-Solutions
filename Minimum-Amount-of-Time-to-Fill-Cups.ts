1function fillCups(amount: number[]): number {
2    amount.sort((a, b) => a - b);
3    const [a, b, c] = amount;
4
5    return Math.max(c, Math.ceil((a + b + c) / 2));
6}