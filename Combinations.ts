1function combine(n: number, k: number): number[][] {
2    const res: number[][] = [];
3
4    function dfs(start: number, path: number[]) {
5        if (path.length === k) {
6            res.push([...path]);
7            return;
8        }
9        for (let i = start; i <= n; i++) {
10            path.push(i);
11            dfs(i + 1, path);
12            path.pop();
13        }
14    }
15
16    dfs(1, []);
17    return res;
18}