1function twoOutOfThree(nums1: number[], nums2: number[], nums3: number[]): number[] {
2    const count = new Map<number, number>();
3
4    for (const set of [new Set(nums1), new Set(nums2), new Set(nums3)]) {
5        for (const num of set) {
6            count.set(num, (count.get(num) || 0) + 1);
7        }
8    }
9
10    return [...count.entries()]
11        .filter(([_, v]) => v >= 2)
12        .map(([k]) => k);
13}