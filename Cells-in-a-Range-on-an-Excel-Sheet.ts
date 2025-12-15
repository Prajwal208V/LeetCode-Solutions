1function cellsInRange(s: string): string[] {
2    const [c1, r1, , c2, r2] = s;
3    const res: string[] = [];
4
5    for (let c = c1.charCodeAt(0); c <= c2.charCodeAt(0); c++) {
6        for (let r = Number(r1); r <= Number(r2); r++) {
7            res.push(String.fromCharCode(c) + r);
8        }
9    }
10    return res;
11}