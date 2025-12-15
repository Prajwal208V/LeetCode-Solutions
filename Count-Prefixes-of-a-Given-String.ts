1function countPrefixes(words: string[], s: string): number {
2    let count = 0;
3
4    for (const word of words) {
5        if (s.startsWith(word)) count++;
6    }
7
8    return count;
9}