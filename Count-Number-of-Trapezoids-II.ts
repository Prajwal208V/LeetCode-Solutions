1function countTrapezoids(points: number[][]): number {
2    const n = points.length;
3    const cnt1: Map<number, Map<number, number>> = new Map();
4    const cnt2: Map<number, Map<number, number>> = new Map();
5
6    for (let i = 0; i < n; i++) {
7        const [x1, y1] = points[i];
8        for (let j = 0; j < i; j++) {
9            const [x2, y2] = points[j];
10            const dx = x2 - x1;
11            const dy = y2 - y1;
12
13            const k = dx === 0 ? 1e9 : dy / dx;
14            const b = dx === 0 ? x1 : (y1 * dx - x1 * dy) / dx;
15
16            if (!cnt1.has(k)) cnt1.set(k, new Map());
17            const mapB = cnt1.get(k)!;
18            mapB.set(b, (mapB.get(b) || 0) + 1);
19
20            const p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
21            if (!cnt2.has(p)) cnt2.set(p, new Map());
22            const mapK = cnt2.get(p)!;
23            mapK.set(k, (mapK.get(k) || 0) + 1);
24        }
25    }
26
27    let ans = 0;
28    for (const e of cnt1.values()) {
29        let s = 0;
30        for (const t of e.values()) {
31            ans += s * t;
32            s += t;
33        }
34    }
35    for (const e of cnt2.values()) {
36        let s = 0;
37        for (const t of e.values()) {
38            ans -= s * t;
39            s += t;
40        }
41    }
42    return ans;
43}
44