1function divideArray(nums: number[]): boolean {
2    const map = new Map<number, number>();
3
4    for (const n of nums) {
5        map.set(n, (map.get(n) || 0) + 1);
6    }
7
8    for (const v of map.values()) {
9        if (v % 2 !== 0) return false;
10    }
11    return true;
12}