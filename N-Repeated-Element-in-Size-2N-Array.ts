1function repeatedNTimes(nums: number[]): number {
2    const seen = new Set<number>();
3    for (const x of nums) {
4        if (seen.has(x)) return x;
5        seen.add(x);
6    }
7    return -1;
8}
9