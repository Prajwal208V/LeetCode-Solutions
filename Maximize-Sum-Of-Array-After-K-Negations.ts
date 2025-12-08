1function largestSumAfterKNegations(nums: number[], k: number): number {
2    nums.sort((a, b) => a - b);
3
4    for (let i = 0; i < nums.length && k > 0; i++) {
5        if (nums[i] < 0) {
6            nums[i] = -nums[i];
7            k--;
8        } else {
9            break;
10        }
11    }
12
13    let sum = 0;
14    let mn = Infinity;
15    for (const x of nums) {
16        sum += x;
17        if (x < mn) mn = x;
18    }
19
20    if (k % 2 === 1) sum -= 2 * mn;
21    return sum;
22}
23