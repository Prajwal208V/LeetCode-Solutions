1function findDifference(nums1: number[], nums2: number[]): number[][] {
2    const s1 = new Set(nums1);
3    const s2 = new Set(nums2);
4
5    const a: number[] = [];
6    const b: number[] = [];
7
8    for (const n of s1) if (!s2.has(n)) a.push(n);
9    for (const n of s2) if (!s1.has(n)) b.push(n);
10
11    return [a, b];
12}