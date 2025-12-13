1function thousandSeparator(n: number): string {
2    const s = n.toString();
3    let res = "";
4    let count = 0;
5
6    for (let i = s.length - 1; i >= 0; i--) {
7        res = s[i] + res;
8        count++;
9        if (count === 3 && i !== 0) {
10            res = "." + res;
11            count = 0;
12        }
13    }
14
15    return res;
16}