1function missingNumber(nums: number[]): number {
2    const n = nums.length;
3    const expected = (n * (n + 1)) / 2;
4    let sum = 0;
5    for (const x of nums) sum += x;
6    return expected - sum;
7}
8