1function divideString(s: string, k: number, fill: string): string[] {
2    const res: string[] = [];
3    for (let i = 0; i < s.length; i += k) {
4        let part = s.slice(i, i + k);
5        if (part.length < k) part += fill.repeat(k - part.length);
6        res.push(part);
7    }
8    return res;
9}