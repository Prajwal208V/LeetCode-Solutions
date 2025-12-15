1function countValidWords(sentence: string): number {
2    const words = sentence.trim().split(/\s+/);
3    let count = 0;
4
5    for (const w of words) {
6        if (w.length === 0) continue;
7        if (/\d/.test(w)) continue;
8        if ((w.match(/-/g) || []).length > 1) continue;
9        if (/-/.test(w) && !/^[a-z]+(-[a-z]+)?[!.,]?$/.test(w)) continue;
10        if (/[!.,]/g.test(w.slice(0, -1))) continue;
11        count++;
12    }
13    return count;
14}