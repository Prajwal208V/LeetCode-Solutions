1function construct2DArray(original: number[], m: number, n: number): number[][] {
2    if (original.length !== m * n) return [];
3
4    const result: number[][] = [];
5    for (let i = 0; i < m; i++) {
6        result.push(original.slice(i * n, (i + 1) * n));
7    }
8
9    return result;
10}