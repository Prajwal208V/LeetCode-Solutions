1function maxSubsequence(nums: number[], k: number): number[] {
2    const indexed = nums.map((v, i) => [v, i]);
3    indexed.sort((a, b) => b[0] - a[0]);
4
5    const top = indexed.slice(0, k).sort((a, b) => a[1] - b[1]);
6    return top.map(x => x[0]);
7}
8