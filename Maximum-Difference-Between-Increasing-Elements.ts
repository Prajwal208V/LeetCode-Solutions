1function maximumDifference(nums: number[]): number {
2    let minVal = nums[0];
3    let maxDiff = -1;
4
5    for (let i = 1; i < nums.length; i++) {
6        if (nums[i] > minVal) {
7            maxDiff = Math.max(maxDiff, nums[i] - minVal);
8        } else {
9            minVal = nums[i];
10        }
11    }
12
13    return maxDiff;
14}