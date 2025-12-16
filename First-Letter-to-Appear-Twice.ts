1function repeatedCharacter(s: string): string {
2    const seen = new Set<string>();
3    for (const ch of s) {
4        if (seen.has(ch)) return ch;
5        seen.add(ch);
6    }
7    return "";
8}