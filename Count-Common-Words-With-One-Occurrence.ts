1function countWords(words1: string[], words2: string[]): number {
2    const m1 = new Map<string, number>();
3    const m2 = new Map<string, number>();
4
5    for (const w of words1) m1.set(w, (m1.get(w) || 0) + 1);
6    for (const w of words2) m2.set(w, (m2.get(w) || 0) + 1);
7
8    let count = 0;
9    for (const [k, v] of m1) {
10        if (v === 1 && m2.get(k) === 1) count++;
11    }
12    return count;
13}