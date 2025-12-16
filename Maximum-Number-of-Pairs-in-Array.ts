1function numberOfPairs(nums: number[]): number[] {
2    const freq = new Map<number, number>();
3    for (const n of nums) freq.set(n, (freq.get(n) || 0) + 1);
4
5    let pairs = 0;
6    let leftovers = 0;
7
8    for (const count of freq.values()) {
9        pairs += Math.floor(count / 2);
10        leftovers += count % 2;
11    }
12
13    return [pairs, leftovers];
14}