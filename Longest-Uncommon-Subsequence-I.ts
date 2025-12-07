1function findLUSlength(a: string, b: string): number {
2    if (a === b) return -1;
3    return Math.max(a.length, b.length);
4}
5