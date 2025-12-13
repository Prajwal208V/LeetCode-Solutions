1function minStartValue(nums: number[]): number {
2    let sum = 0;
3    let minSum = 0;
4
5    for (const num of nums) {
6        sum += num;
7        minSum = Math.min(minSum, sum);
8    }
9
10    return 1 - minSum;
11}