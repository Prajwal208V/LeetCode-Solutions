1function integerBreak(n: number): number {
2    if (n === 2) return 1;
3    if (n === 3) return 2;
4    let count3 = Math.floor(n / 3);
5    if (n - count3 * 3 === 1) count3--;
6    const remainder = n - count3 * 3;
7    const count2 = Math.floor(remainder / 2);
8    return Math.pow(3, count3) * Math.pow(2, count2);
9}
10