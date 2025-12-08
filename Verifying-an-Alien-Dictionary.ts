1function isAlienSorted(words: string[], order: string): boolean {
2    const rank: number[] = new Array(26).fill(0);
3    for (let i = 0; i < order.length; i++) {
4        rank[order.charCodeAt(i) - 97] = i;
5    }
6
7    function inOrder(a: string, b: string): boolean {
8        const m = Math.min(a.length, b.length);
9        for (let i = 0; i < m; i++) {
10            const ca = rank[a.charCodeAt(i) - 97];
11            const cb = rank[b.charCodeAt(i) - 97];
12            if (ca < cb) return true;
13            if (ca > cb) return false;
14        }
15        return a.length <= b.length;
16    }
17
18    for (let i = 1; i < words.length; i++) {
19        if (!inOrder(words[i - 1], words[i])) return false;
20    }
21    return true;
22}
23