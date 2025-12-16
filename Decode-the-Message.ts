1function decodeMessage(key: string, message: string): string {
2    const map = new Map<string, string>();
3    let ch = 97;
4
5    for (const c of key) {
6        if (c !== ' ' && !map.has(c)) {
7            map.set(c, String.fromCharCode(ch++));
8        }
9    }
10
11    let res = "";
12    for (const c of message) {
13        res += c === ' ' ? ' ' : map.get(c);
14    }
15    return res;
16}