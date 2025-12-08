1function sortArrayByParityII(nums: number[]): number[] {
2    let i = 0, j = 1;
3    const n = nums.length;
4
5    while (i < n && j < n) {
6        if (nums[i] % 2 === 0) i += 2;
7        else if (nums[j] % 2 === 1) j += 2;
8        else {
9            [nums[i], nums[j]] = [nums[j], nums[i]];
10            i += 2;
11            j += 2;
12        }
13    }
14
15    return nums;
16}