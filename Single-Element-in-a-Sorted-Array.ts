1function singleNonDuplicate(nums: number[]): number {
2    let l = 0, r = nums.length - 1;
3    while (l < r) {
4        let mid = Math.floor((l + r) / 2);
5        if (mid % 2 === 1) mid--;
6        if (nums[mid] === nums[mid + 1]) l = mid + 2;
7        else r = mid;
8    }
9    return nums[l];
10}