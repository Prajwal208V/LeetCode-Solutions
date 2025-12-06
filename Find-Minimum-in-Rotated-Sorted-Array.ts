1function findMin(nums: number[]): number {
2    let left = 0, right = nums.length - 1;
3
4    while (left < right) {
5        const mid = (left + right) >> 1;
6        if (nums[mid] > nums[right]) left = mid + 1;
7        else right = mid;
8    }
9
10    return nums[left];
11}