1function diStringMatch(s: string): number[] {
2    let low = 0, high = s.length;
3    const res: number[] = [];
4
5    for (const ch of s) {
6        if (ch === 'I') {
7            res.push(low++);
8        } else {
9            res.push(high--);
10        }
11    }
12
13    res.push(low);
14    return res;
15}
16