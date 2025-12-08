1function fairCandySwap(aliceSizes: number[], bobSizes: number[]): number[] {
2    const sumA = aliceSizes.reduce((a, b) => a + b, 0);
3    const sumB = bobSizes.reduce((a, b) => a + b, 0);
4    const diff = (sumA - sumB) / 2;
5
6    const setA = new Set<number>(aliceSizes);
7
8    for (const b of bobSizes) {
9        const a = b + diff;
10        if (setA.has(a)) {
11            return [a, b];
12        }
13    }
14
15    return [];
16}
17