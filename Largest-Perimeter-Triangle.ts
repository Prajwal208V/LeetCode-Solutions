1function largestPerimeter(nums: number[]): number {
2    nums.sort((a, b) => a - b);
3    for (let i = nums.length - 1; i >= 2; i--) {
4        if (nums[i - 2] + nums[i - 1] > nums[i]) {
5            return nums[i - 2] + nums[i - 1] + nums[i];
6        }
7    }
8    return 0;
9}
10