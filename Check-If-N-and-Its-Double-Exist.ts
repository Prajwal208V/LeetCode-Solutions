1function checkIfExist(arr: number[]): boolean {
2    const seen = new Set<number>();
3
4    for (const num of arr) {
5        if (seen.has(num * 2) || (num % 2 === 0 && seen.has(num / 2))) {
6            return true;
7        }
8        seen.add(num);
9    }
10
11    return false;
12}