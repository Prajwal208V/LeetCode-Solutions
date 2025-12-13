1function maxLengthBetweenEqualCharacters(s: string): number {
2    const firstIndex = new Map<string, number>();
3    let maxLen = -1;
4
5    for (let i = 0; i < s.length; i++) {
6        if (firstIndex.has(s[i])) {
7            maxLen = Math.max(maxLen, i - firstIndex.get(s[i])! - 1);
8        } else {
9            firstIndex.set(s[i], i);
10        }
11    }
12
13    return maxLen;
14}