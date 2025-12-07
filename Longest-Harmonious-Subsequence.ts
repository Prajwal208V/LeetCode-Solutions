1function findLHS(nums: number[]): number {
2    const map = new Map<number, number>();
3    for (const x of nums) map.set(x, (map.get(x) || 0) + 1);
4    let ans = 0;
5    for (const [k, v] of map.entries()) {
6        if (map.has(k + 1)) {
7            ans = Math.max(ans, v + (map.get(k + 1) || 0));
8        }
9    }
10    return ans;
11}
12