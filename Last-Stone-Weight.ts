1function lastStoneWeight(stones: number[]): number {
2    class MaxHeap {
3        data: number[] = [];
4        push(x: number) {
5            this.data.push(x);
6            let i = this.data.length - 1;
7            while (i > 0) {
8                const p = (i - 1) >> 1;
9                if (this.data[p] >= this.data[i]) break;
10                [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
11                i = p;
12            }
13        }
14        pop(): number | undefined {
15            if (this.data.length === 0) return undefined;
16            const top = this.data[0];
17            const last = this.data.pop()!;
18            if (this.data.length > 0) {
19                this.data[0] = last;
20                let i = 0;
21                const n = this.data.length;
22                while (true) {
23                    let largest = i;
24                    const l = i * 2 + 1;
25                    const r = i * 2 + 2;
26                    if (l < n && this.data[l] > this.data[largest]) largest = l;
27                    if (r < n && this.data[r] > this.data[largest]) largest = r;
28                    if (largest === i) break;
29                    [this.data[i], this.data[largest]] = [this.data[largest], this.data[i]];
30                    i = largest;
31                }
32            }
33            return top;
34        }
35        size(): number {
36            return this.data.length;
37        }
38    }
39
40    const h = new MaxHeap();
41    for (const s of stones) h.push(s);
42
43    while (h.size() > 1) {
44        const y = h.pop()!;
45        const x = h.pop()!;
46        if (y > x) h.push(y - x);
47    }
48
49    return h.size() === 0 ? 0 : h.pop()!;
50}
51