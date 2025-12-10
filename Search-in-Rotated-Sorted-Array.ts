1function search(nums: number[], target: number): number {
2    let left = 0;
3    let right = nums.length - 1;
4
5    while (left <= right) {
6        const mid = left + ((right - left) >> 1);
7        if (nums[mid] === target) return mid;
8
9        if (nums[left] <= nums[mid]) {
10            if (nums[left] <= target && target < nums[mid]) {
11                right = mid - 1;
12            } else {
13                left = mid + 1;
14            }
15        } else {
16            if (nums[mid] < target && target <= nums[right]) {
17                left = mid + 1;
18            } else {
19                right = mid - 1;
20            }
21        }
22    }
23
24    return -1;
25}