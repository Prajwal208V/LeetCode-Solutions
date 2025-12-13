1function specialArray(nums: number[]): number {
2    nums.sort((a, b) => a - b);
3    const n = nums.length;
4
5    for (let x = 1; x <= n; x++) {
6        const idx = n - x;
7        if (nums[idx] >= x && (idx === 0 || nums[idx - 1] < x)) {
8            return x;
9        }
10    }
11
12    return -1;
13}