1function findKDistantIndices(nums: number[], key: number, k: number): number[] {
2    const res: number[] = [];
3    const idx: number[] = [];
4
5    for (let i = 0; i < nums.length; i++) {
6        if (nums[i] === key) idx.push(i);
7    }
8
9    for (let i = 0; i < nums.length; i++) {
10        for (const j of idx) {
11            if (Math.abs(i - j) <= k) {
12                res.push(i);
13                break;
14            }
15        }
16    }
17    return res;
18}