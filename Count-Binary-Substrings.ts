1function countBinarySubstrings(s: string): number {
2    let prev = 0, cur = 1, res = 0;
3    for (let i = 1; i < s.length; i++) {
4        if (s[i] === s[i - 1]) cur++;
5        else {
6            res += Math.min(prev, cur);
7            prev = cur;
8            cur = 1;
9        }
10    }
11    res += Math.min(prev, cur);
12    return res;
13}
14