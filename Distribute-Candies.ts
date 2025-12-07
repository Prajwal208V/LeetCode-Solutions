1function distributeCandies(candyType: number[]): number {
2    const kinds = new Set(candyType).size;
3    const maxEat = candyType.length / 2;
4    return Math.min(kinds, maxEat);
5}
6