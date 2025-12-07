1function longestPalindrome(s: string): number {
2    const cnt = new Map<string, number>();
3    for (const c of s) cnt.set(c, (cnt.get(c) || 0) + 1);
4
5    let res = 0;
6    let odd = false;
7
8    for (const v of cnt.values()) {
9        res += Math.floor(v / 2) * 2;
10        if (v % 2 === 1) odd = true;
11    }
12
13    return odd ? res + 1 : res;
14}
15