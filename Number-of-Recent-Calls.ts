1class RecentCounter {
2    q: number[];
3
4    constructor() {
5        this.q = [];
6    }
7
8    ping(t: number): number {
9        this.q.push(t);
10        while (this.q[0] < t - 3000) this.q.shift();
11        return this.q.length;
12    }
13}
14
15
16/**
17 * Your RecentCounter object will be instantiated and called as such:
18 * var obj = new RecentCounter()
19 * var param_1 = obj.ping(t)
20 */