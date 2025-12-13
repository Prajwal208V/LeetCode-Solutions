1function maxProduct(nums: number[]): number {
2    let max1 = 0;
3    let max2 = 0;
4
5    for (const num of nums) {
6        if (num > max1) {
7            max2 = max1;
8            max1 = num;
9        } else if (num > max2) {
10            max2 = num;
11        }
12    }
13
14    return (max1 - 1) * (max2 - 1);
15}