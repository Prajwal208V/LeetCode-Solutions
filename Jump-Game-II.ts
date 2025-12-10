1function jump(nums: number[]): number {
2    let jumps = 0;
3    let currentEnd = 0;
4    let farthest = 0;
5
6    for (let i = 0; i < nums.length - 1; i++) {
7        farthest = Math.max(farthest, i + nums[i]);
8        if (i === currentEnd) {
9            jumps++;
10            currentEnd = farthest;
11        }
12    }
13
14    return jumps;
15}
16