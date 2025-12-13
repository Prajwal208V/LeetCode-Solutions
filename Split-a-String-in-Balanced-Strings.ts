1function balancedStringSplit(s: string): number {
2    let balance = 0;
3    let count = 0;
4
5    for (const ch of s) {
6        if (ch === 'L') balance++;
7        else balance--;
8
9        if (balance === 0) count++;
10    }
11
12    return count;
13}