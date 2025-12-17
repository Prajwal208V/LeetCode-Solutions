1class Solution {
2    private prefix: number[]
3    private total: number
4
5    constructor(w: number[]) {
6        this.prefix = []
7        this.total = 0
8        for (const x of w) {
9            this.total += x
10            this.prefix.push(this.total)
11        }
12    }
13
14    pickIndex(): number {
15        const r = Math.random() * this.total
16        let l = 0, h = this.prefix.length - 1
17        while (l < h) {
18            const m = Math.floor((l + h) / 2)
19            if (r < this.prefix[m]) h = m
20            else l = m + 1
21        }
22        return l
23    }
24}
25
26/**
27 * Your Solution object will be instantiated and called as such:
28 * var obj = new Solution(w)
29 * var param_1 = obj.pickIndex()
30 */