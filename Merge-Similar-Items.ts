1function mergeSimilarItems(items1: number[][], items2: number[][]): number[][] {
2    const map = new Map<number, number>();
3
4    for (const [v, w] of items1) map.set(v, (map.get(v) || 0) + w);
5    for (const [v, w] of items2) map.set(v, (map.get(v) || 0) + w);
6
7    return Array.from(map.entries())
8        .sort((a, b) => a[0] - b[0])
9        .map(([v, w]) => [v, w]);
10}