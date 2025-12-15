1function findClosestNumber(nums: number[]): number {
2    let res = nums[0];
3
4    for (const n of nums) {
5        if (
6            Math.abs(n) < Math.abs(res) ||
7            (Math.abs(n) === Math.abs(res) && n > res)
8        ) {
9            res = n;
10        }
11    }
12    return res;
13}