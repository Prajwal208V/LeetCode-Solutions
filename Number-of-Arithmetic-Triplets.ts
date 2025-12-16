1function arithmeticTriplets(nums: number[], diff: number): number {
2    const set = new Set(nums);
3    let count = 0;
4
5    for (const n of nums) {
6        if (set.has(n + diff) && set.has(n + 2 * diff)) {
7            count++;
8        }
9    }
10    return count;
11}