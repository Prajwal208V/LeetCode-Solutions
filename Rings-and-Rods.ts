1function countPoints(rings: string): number {
2    const map = new Map<number, Set<string>>();
3
4    for (let i = 0; i < rings.length; i += 2) {
5        const color = rings[i];
6        const rod = Number(rings[i + 1]);
7        if (!map.has(rod)) map.set(rod, new Set());
8        map.get(rod)!.add(color);
9    }
10
11    let count = 0;
12    for (const set of map.values()) {
13        if (set.size === 3) count++;
14    }
15    return count;
16}