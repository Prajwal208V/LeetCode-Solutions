1function nthUglyNumber(n: number): number {
2    const dp: number[] = new Array(n);
3    dp[0] = 1;
4    let i2 = 0, i3 = 0, i5 = 0;
5
6    for (let i = 1; i < n; i++) {
7        const next2 = dp[i2] * 2;
8        const next3 = dp[i3] * 3;
9        const next5 = dp[i5] * 5;
10        const next = Math.min(next2, next3, next5);
11        dp[i] = next;
12        if (next === next2) i2++;
13        if (next === next3) i3++;
14        if (next === next5) i5++;
15    }
16
17    return dp[n - 1];
18}
19