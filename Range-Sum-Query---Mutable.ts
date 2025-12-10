1class NumArray {
2    private n: number;
3    private bit: number[];
4    private nums: number[];
5
6    constructor(nums: number[]) {
7        this.n = nums.length;
8        this.bit = new Array(this.n + 1).fill(0);
9        this.nums = nums.slice();
10        for (let i = 0; i < this.n; i++) {
11            this.add(i + 1, nums[i]);
12        }
13    }
14
15    private add(i: number, delta: number): void {
16        while (i <= this.n) {
17            this.bit[i] += delta;
18            i += i & -i;
19        }
20    }
21
22    update(index: number, val: number): void {
23        const delta = val - this.nums[index];
24        this.nums[index] = val;
25        this.add(index + 1, delta);
26    }
27
28    private prefixSum(i: number): number {
29        let s = 0;
30        while (i > 0) {
31            s += this.bit[i];
32            i -= i & -i;
33        }
34        return s;
35    }
36
37    sumRange(left: number, right: number): number {
38        return this.prefixSum(right + 1) - this.prefixSum(left + 1 - 1);
39    }
40}
41
42/**
43 * Your NumArray object will be instantiated and called as such:
44 * var obj = new NumArray(nums)
45 * obj.update(index,val)
46 * var param_2 = obj.sumRange(left,right)
47 */