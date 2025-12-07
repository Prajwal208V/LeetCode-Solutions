1function arrayPairSum(nums: number[]): number {
2    nums.sort((a, b) => a - b);
3    let sum = 0;
4    for (let i = 0; i < nums.length; i += 2) {
5        sum += nums[i];
6    }
7    return sum;
8}
9