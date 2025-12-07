1function lengthOfLastWord(s: string): number {
2    let i = s.length - 1;
3    while (i >= 0 && s[i] === ' ') i--;
4    let len = 0;
5    while (i >= 0 && s[i] !== ' ') {
6        len++;
7        i--;
8    }
9    return len;
10}
11