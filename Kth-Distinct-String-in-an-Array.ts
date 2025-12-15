1function kthDistinct(arr: string[], k: number): string {
2    const freq = new Map<string, number>();
3    for (const s of arr) freq.set(s, (freq.get(s) || 0) + 1);
4
5    for (const s of arr) {
6        if (freq.get(s) === 1) {
7            k--;
8            if (k === 0) return s;
9        }
10    }
11    return "";
12}