1function search(nums: number[], target: number): boolean {
2    let left = 0;
3    let right = nums.length - 1;
4
5    while (left <= right) {
6        const mid = left + ((right - left) >> 1);
7        if (nums[mid] === target) return true;
8
9        if (nums[left] === nums[mid] && nums[mid] === nums[right]) {
10            left++;
11            right--;
12        } else if (nums[left] <= nums[mid]) {
13            if (nums[left] <= target && target < nums[mid]) {
14                right = mid - 1;
15            } else {
16                left = mid + 1;
17            }
18        } else {
19            if (nums[mid] < target && target <= nums[right]) {
20                left = mid + 1;
21            } else {
22                right = mid - 1;
23            }
24        }
25    }
26
27    return false;
28}