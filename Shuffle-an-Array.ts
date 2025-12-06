1class Solution {
2    original: number[];
3    arr: number[];
4
5    constructor(nums: number[]) {
6        this.original = nums.slice();
7        this.arr = nums.slice();
8    }
9
10    reset(): number[] {
11        this.arr = this.original.slice();
12        return this.arr;
13    }
14
15    shuffle(): number[] {
16        const res = this.arr.slice();
17        for (let i = res.length - 1; i > 0; i--) {
18            const j = Math.floor(Math.random() * (i + 1));
19            [res[i], res[j]] = [res[j], res[i]];
20        }
21        return res;
22    }
23}
24
25/**
26 * Your Solution object will be instantiated and called as such:
27 * var obj = new Solution(nums)
28 * var param_1 = obj.reset()
29 * var param_2 = obj.shuffle()
30 */