1function maxPower(s: string): number {
2    let maxLen = 1;
3    let currLen = 1;
4
5    for (let i = 1; i < s.length; i++) {
6        if (s[i] === s[i - 1]) {
7            currLen++;
8            maxLen = Math.max(maxLen, currLen);
9        } else {
10            currLen = 1;
11        }
12    }
13
14    return maxLen;
15}