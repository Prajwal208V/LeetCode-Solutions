1function climbStairs(n: number): number {
2    if (n <= 2) return n;
3    let a = 1, b = 2;
4    for (let i = 3; i <= n; i++) {
5        const c = a + b;
6        a = b;
7        b = c;
8    }
9    return b;
10}
11