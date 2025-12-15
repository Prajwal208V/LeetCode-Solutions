1function countHillValley(nums: number[]): number {
2    let count = 0;
3    let prev = nums[0];
4
5    for (let i = 1; i < nums.length - 1; i++) {
6        if (nums[i] === nums[i + 1]) continue;
7
8        if (
9            (nums[i] > prev && nums[i] > nums[i + 1]) ||
10            (nums[i] < prev && nums[i] < nums[i + 1])
11        ) {
12            count++;
13            prev = nums[i];
14        }
15    }
16    return count;
17}