1function reformat(s: string): string {
2    const letters: string[] = [];
3    const digits: string[] = [];
4
5    for (const ch of s) {
6        if (ch >= '0' && ch <= '9') digits.push(ch);
7        else letters.push(ch);
8    }
9
10    if (Math.abs(letters.length - digits.length) > 1) {
11        return "";
12    }
13
14    let res: string[] = [];
15    let i = 0;
16
17    let first = letters.length >= digits.length ? letters : digits;
18    let second = letters.length >= digits.length ? digits : letters;
19
20    while (i < first.length || i < second.length) {
21        if (i < first.length) res.push(first[i]);
22        if (i < second.length) res.push(second[i]);
23        i++;
24    }
25
26    return res.join("");
27}