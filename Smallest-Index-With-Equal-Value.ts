1function smallestEqual(nums: number[]): number {
2    for (let i = 0; i < nums.length; i++) {
3        if (i % 10 === nums[i]) return i;
4    }
5    return -1;
6}