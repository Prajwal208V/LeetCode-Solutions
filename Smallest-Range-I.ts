1function smallestRangeI(nums: number[], k: number): number {
2    let mn = Infinity, mx = -Infinity;
3    for (const x of nums) {
4        if (x < mn) mn = x;
5        if (x > mx) mx = x;
6    }
7    const diff = mx - mn - 2 * k;
8    return diff > 0 ? diff : 0;
9}
10