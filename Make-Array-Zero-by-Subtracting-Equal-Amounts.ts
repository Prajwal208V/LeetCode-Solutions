1function minimumOperations(nums: number[]): number {
2    const set = new Set<number>();
3    for (const n of nums) {
4        if (n > 0) set.add(n);
5    }
6    return set.size;
7}