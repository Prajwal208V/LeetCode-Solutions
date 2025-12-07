1function exist(board: string[][], word: string): boolean {
2    const m = board.length;
3    const n = board[0].length;
4    const w = word.length;
5
6    function dfs(i: number, j: number, k: number): boolean {
7        if (k === w) return true;
8        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== word[k]) return false;
9
10        const tmp = board[i][j];
11        board[i][j] = "#";
12
13        const found =
14            dfs(i + 1, j, k + 1) ||
15            dfs(i - 1, j, k + 1) ||
16            dfs(i, j + 1, k + 1) ||
17            dfs(i, j - 1, k + 1);
18
19        board[i][j] = tmp;
20        return found;
21    }
22
23    for (let i = 0; i < m; i++) {
24        for (let j = 0; j < n; j++) {
25            if (dfs(i, j, 0)) return true;
26        }
27    }
28    return false;
29}
30