1function canBeEqual(target: number[], arr: number[]): boolean {
2    const count = new Map<number, number>();
3
4    for (const num of target) {
5        count.set(num, (count.get(num) || 0) + 1);
6    }
7
8    for (const num of arr) {
9        if (!count.has(num)) return false;
10        count.set(num, count.get(num)! - 1);
11        if (count.get(num) === 0) count.delete(num);
12    }
13
14    return count.size === 0;
15}