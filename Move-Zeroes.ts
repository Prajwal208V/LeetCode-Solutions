1/**
2 Do not return anything, modify nums in-place instead.
3 */
4function moveZeroes(nums: number[]): void {
5    let j = 0;
6    for (let i = 0; i < nums.length; i++) {
7        if (nums[i] !== 0) {
8            [nums[i], nums[j]] = [nums[j], nums[i]];
9            j++;
10        }
11    }
12}
13