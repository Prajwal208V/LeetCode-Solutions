1class NumArray {
2    pref: number[];
3
4    constructor(nums: number[]) {
5        this.pref = [0];
6        for (const x of nums) this.pref.push(this.pref[this.pref.length - 1] + x);
7    }
8
9    sumRange(left: number, right: number): number {
10        return this.pref[right + 1] - this.pref[left];
11    }
12}
13
14
15/**
16 * Your NumArray object will be instantiated and called as such:
17 * var obj = new NumArray(nums)
18 * var param_1 = obj.sumRange(left,right)
19 */