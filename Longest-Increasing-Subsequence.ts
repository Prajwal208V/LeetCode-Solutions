1function lengthOfLIS(nums: number[]): number {
2    const tails: number[] = [];
3    for (const x of nums) {
4        let l = 0;
5        let r = tails.length;
6        while (l < r) {
7            const m = (l + r) >> 1;
8            if (tails[m] < x) l = m + 1;
9            else r = m;
10        }
11        if (l === tails.length) tails.push(x);
12        else tails[l] = x;
13    }
14    return tails.length;
15}