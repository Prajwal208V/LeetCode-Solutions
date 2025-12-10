1/**
2 Do not return anything, modify nums in-place instead.
3 */
4function nextPermutation(nums: number[]): void {
5    const n = nums.length;
6    let i = n - 2;
7    while (i >= 0 && nums[i] >= nums[i + 1]) i--;
8    if (i >= 0) {
9        let j = n - 1;
10        while (j >= 0 && nums[j] <= nums[i]) j--;
11        [nums[i], nums[j]] = [nums[j], nums[i]];
12    }
13    let l = i + 1;
14    let r = n - 1;
15    while (l < r) {
16        [nums[l], nums[r]] = [nums[r], nums[l]];
17        l++;
18        r--;
19    }
20}
21