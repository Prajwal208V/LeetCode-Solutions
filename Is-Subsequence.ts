1function isSubsequence(s: string, t: string): boolean {
2    let i = 0, j = 0;
3    while (i < s.length && j < t.length) {
4        if (s[i] === t[j]) i++;
5        j++;
6    }
7    return i === s.length;
8}
9