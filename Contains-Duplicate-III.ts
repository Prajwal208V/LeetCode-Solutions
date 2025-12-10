1function containsNearbyAlmostDuplicate(nums: number[], indexDiff: number, valueDiff: number): boolean {
2    if (indexDiff < 0 || valueDiff < 0) return false;
3    const bucketSize = valueDiff + 1;
4    const buckets = new Map<number, number>();
5    const getId = (x: number) => Math.floor(x / bucketSize);
6
7    for (let i = 0; i < nums.length; i++) {
8        if (i > indexDiff) {
9            const oldId = getId(nums[i - indexDiff - 1]);
10            buckets.delete(oldId);
11        }
12        const x = nums[i];
13        const id = getId(x);
14        if (buckets.has(id)) return true;
15        if (buckets.has(id - 1) && Math.abs(x - (buckets.get(id - 1) as number)) <= valueDiff) return true;
16        if (buckets.has(id + 1) && Math.abs(x - (buckets.get(id + 1) as number)) <= valueDiff) return true;
17        buckets.set(id, x);
18    }
19
20    return false;
21}
22