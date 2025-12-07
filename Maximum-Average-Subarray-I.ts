1function findMaxAverage(nums: number[], k: number): number {
2    let sum = 0;
3    for (let i = 0; i < k; i++) sum += nums[i];
4    let maxSum = sum;
5
6    for (let i = k; i < nums.length; i++) {
7        sum += nums[i] - nums[i - k];
8        if (sum > maxSum) maxSum = sum;
9    }
10
11    return maxSum / k;
12}
13