1function removeAnagrams(words: string[]): string[] {
2    const res: string[] = [];
3    let prev = "";
4
5    for (const w of words) {
6        const sorted = w.split('').sort().join('');
7        if (sorted !== prev) {
8            res.push(w);
9            prev = sorted;
10        }
11    }
12    return res;
13}