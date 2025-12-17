1class Solution {
2    private rows: number
3    private cols: number
4    private total: number
5    private map: Map<number, number>
6
7    constructor(m: number, n: number) {
8        this.rows = m
9        this.cols = n
10        this.total = m * n
11        this.map = new Map()
12    }
13
14    flip(): number[] {
15        const r = Math.floor(Math.random() * this.total)
16        this.total--
17
18        const idx = this.map.get(r) ?? r
19        this.map.set(r, this.map.get(this.total) ?? this.total)
20
21        return [Math.floor(idx / this.cols), idx % this.cols]
22    }
23
24    reset(): void {
25        this.total = this.rows * this.cols
26        this.map.clear()
27    }
28}
29
30/**
31 * Your Solution object will be instantiated and called as such:
32 * var obj = new Solution(m, n)
33 * var param_1 = obj.flip()
34 * obj.reset()
35 */