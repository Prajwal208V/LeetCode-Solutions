1function findCircleNum(isConnected: number[][]): number {
2    const n = isConnected.length;
3    const seen = new Array(n).fill(false);
4
5    function dfs(i: number) {
6        for (let j = 0; j < n; j++)
7            if (isConnected[i][j] && !seen[j]) {
8                seen[j] = true;
9                dfs(j);
10            }
11    }
12
13    let count = 0;
14    for (let i = 0; i < n; i++)
15        if (!seen[i]) { seen[i] = true; dfs(i); count++; }
16
17    return count;
18}