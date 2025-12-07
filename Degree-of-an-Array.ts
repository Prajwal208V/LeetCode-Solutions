1function findShortestSubArray(nums: number[]): number {
2    const count = new Map<number, number>();
3    const first = new Map<number, number>();
4    const last = new Map<number, number>();
5
6    for (let i = 0; i < nums.length; i++) {
7        const x = nums[i];
8        if (!first.has(x)) first.set(x, i);
9        last.set(x, i);
10        count.set(x, (count.get(x) || 0) + 1);
11    }
12
13    let degree = 0;
14    for (const v of count.values()) {
15        if (v > degree) degree = v;
16    }
17
18    let res = nums.length;
19    for (const [x, c] of count.entries()) {
20        if (c === degree) {
21            const len = (last.get(x)! - first.get(x)!) + 1;
22            if (len < res) res = len;
23        }
24    }
25
26    return res;
27}
28