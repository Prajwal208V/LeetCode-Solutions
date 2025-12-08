1function sortArrayByParity(nums: number[]): number[] {
2    let l = 0, r = nums.length - 1;
3    while (l < r) {
4        if (nums[l] % 2 > nums[r] % 2) {
5            [nums[l], nums[r]] = [nums[r], nums[l]];
6        }
7        if (nums[l] % 2 === 0) l++;
8        if (nums[r] % 2 === 1) r--;
9    }
10    return nums;
11}
12