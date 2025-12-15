1function mostFrequent(nums: number[], key: number): number {
2    const map = new Map<number, number>();
3
4    for (let i = 0; i < nums.length - 1; i++) {
5        if (nums[i] === key) {
6            map.set(nums[i + 1], (map.get(nums[i + 1]) || 0) + 1);
7        }
8    }
9
10    let res = 0, max = 0;
11    for (const [k, v] of map) {
12        if (v > max) {
13            max = v;
14            res = k;
15        }
16    }
17    return res;
18}