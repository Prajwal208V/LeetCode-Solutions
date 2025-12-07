1function repeatedSubstringPattern(s: string): boolean {
2    const t = (s + s).slice(1, -1);
3    return t.includes(s);
4}
5