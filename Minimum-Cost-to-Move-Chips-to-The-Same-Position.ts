1function minCostToMoveChips(position: number[]): number {
2    let even = 0;
3    let odd = 0;
4
5    for (const p of position) {
6        if (p % 2 === 0) even++;
7        else odd++;
8    }
9
10    return Math.min(even, odd);
11}