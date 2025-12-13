1function mostVisited(n: number, rounds: number[]): number[] {
2    const start = rounds[0];
3    const end = rounds[rounds.length - 1];
4
5    if (start <= end) {
6        const res: number[] = [];
7        for (let i = start; i <= end; i++) {
8            res.push(i);
9        }
10        return res;
11    } else {
12        const res: number[] = [];
13        for (let i = 1; i <= end; i++) res.push(i);
14        for (let i = start; i <= n; i++) res.push(i);
15        return res;
16    }
17}