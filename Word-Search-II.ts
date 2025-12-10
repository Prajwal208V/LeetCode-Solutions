1function findWords(board: string[][], words: string[]): string[] {
2    const root: any = {};
3    for (const w of words) {
4        let node = root;
5        for (const ch of w) {
6            if (!node[ch]) node[ch] = {};
7            node = node[ch];
8        }
9        node.word = w;
10    }
11
12    const m = board.length;
13    if (m === 0) return [];
14    const n = board[0].length;
15    const res: string[] = [];
16
17    function dfs(i: number, j: number, node: any): void {
18        const ch = board[i][j];
19        const next = node[ch];
20        if (!next) return;
21
22        if (next.word) {
23            res.push(next.word);
24            next.word = null;
25        }
26
27        board[i][j] = "#";
28
29        if (i > 0 && board[i - 1][j] !== "#") dfs(i - 1, j, next);
30        if (i < m - 1 && board[i + 1][j] !== "#") dfs(i + 1, j, next);
31        if (j > 0 && board[i][j - 1] !== "#") dfs(i, j - 1, next);
32        if (j < n - 1 && board[i][j + 1] !== "#") dfs(i, j + 1, next);
33
34        board[i][j] = ch;
35
36        if (Object.keys(next).length === 0) {
37            delete node[ch];
38        }
39    }
40
41    for (let i = 0; i < m; i++) {
42        for (let j = 0; j < n; j++) {
43            dfs(i, j, root);
44        }
45    }
46
47    return res;
48}