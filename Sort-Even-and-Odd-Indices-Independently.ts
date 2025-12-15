1function sortEvenOdd(nums: number[]): number[] {
2    const even: number[] = [], odd: number[] = [];
3
4    for (let i = 0; i < nums.length; i++) {
5        (i % 2 === 0 ? even : odd).push(nums[i]);
6    }
7
8    even.sort((a, b) => a - b);
9    odd.sort((a, b) => b - a);
10
11    let e = 0, o = 0;
12    for (let i = 0; i < nums.length; i++) {
13        nums[i] = i % 2 === 0 ? even[e++] : odd[o++];
14    }
15    return nums;
16}