1function checkAlmostEquivalent(word1: string, word2: string): boolean {
2    const cnt = new Array(26).fill(0);
3
4    for (const c of word1) cnt[c.charCodeAt(0) - 97]++;
5    for (const c of word2) cnt[c.charCodeAt(0) - 97]--;
6
7    return cnt.every(v => Math.abs(v) <= 3);
8}