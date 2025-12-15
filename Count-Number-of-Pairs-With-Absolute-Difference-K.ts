1function countKDifference(nums: number[], k: number): number {
2    const map = new Map<number, number>();
3    let count = 0;
4
5    for (const num of nums) {
6        count += (map.get(num - k) || 0) + (map.get(num + k) || 0);
7        map.set(num, (map.get(num) || 0) + 1);
8    }
9
10    return count;
11}