1function readBinaryWatch(turnedOn: number): string[] {
2    const res: string[] = [];
3    for (let h = 0; h < 12; h++) {
4        for (let m = 0; m < 60; m++) {
5            if (bitCount(h) + bitCount(m) === turnedOn) {
6                res.push(`${h}:${m.toString().padStart(2, "0")}`);
7            }
8        }
9    }
10    return res;
11}
12
13function bitCount(x: number): number {
14    let c = 0;
15    while (x) {
16        x &= x - 1;
17        c++;
18    }
19    return c;
20}
21