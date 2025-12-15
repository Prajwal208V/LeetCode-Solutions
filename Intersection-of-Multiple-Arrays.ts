1function intersection(nums: number[][]): number[] {
2    const map = new Map<number, number>();
3
4    for (const arr of nums) {
5        for (const n of new Set(arr)) {
6            map.set(n, (map.get(n) || 0) + 1);
7        }
8    }
9
10    const res: number[] = [];
11    for (const [k, v] of map) {
12        if (v === nums.length) res.push(k);
13    }
14
15    return res.sort((a, b) => a - b);
16}